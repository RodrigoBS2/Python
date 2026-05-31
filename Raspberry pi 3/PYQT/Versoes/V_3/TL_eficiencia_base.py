# -*- coding: utf-8 -*-
"""
Created on Tue May 26 20:16:33 2026

@author: Flávia Eduarda
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.special import factorial
import os
import glob

# =============================================================================
# 1. CARREGAMENTO E LIMPEZA DO FÓTON ESCURO
# =============================================================================

def carregar_dados_reais(diretorio):
    padrao = os.path.join(diretorio, "dados_daq_*.csv")
    arquivos = glob.glob(padrao)

    if not arquivos:
        raise FileNotFoundError("Nenhum arquivo encontrado no diretório especificado.")

    arquivo = max(arquivos, key=os.path.getmtime)
    dados = np.genfromtxt(arquivo, delimiter=',', skip_header=1)

    tempo = dados[:,0]
    sinal_bruto = dados[:,1]

    v_min = np.min(sinal_bruto)
    v_max = np.max(sinal_bruto)
    limiar_escuro = v_min + 0.05 * (v_max - v_min)
    v_escuro = np.mean(sinal_bruto[sinal_bruto < limiar_escuro])
    
    sinal_puro = sinal_bruto - v_escuro

    return tempo, sinal_puro, os.path.basename(arquivo)

# =============================================================================
# 2. RECORTE DO CHOPPER
# =============================================================================

def isolar_pulso(tempo, sinal):
    v_min = np.min(sinal)
    v_max = np.max(sinal)
    limiar = v_min + 0.5 * (v_max - v_min)

    acima = sinal > limiar
    mudancas = np.diff(acima.astype(int))

    bordas_subida = np.where(mudancas == 1)[0]
    bordas_descida = np.where(mudancas == -1)[0]

    if len(bordas_subida) == 0:
        return tempo, sinal

    idx_meio_subida = bordas_subida[0]

    descidas_validas = bordas_descida[bordas_descida > idx_meio_subida]
    idx_descida = descidas_validas[0] if len(descidas_validas) > 0 else len(sinal) - 1

    kernel = np.ones(5)/5.0
    sinal_suave = np.convolve(sinal, kernel, mode='same')
    derivada = np.gradient(sinal_suave)

    inicio_busca = max(0, idx_meio_subida - 10)
    fim_busca = min(len(derivada), idx_meio_subida + 10)
    pico_derivada = np.max(derivada[inicio_busca:fim_busca])

    idx_inicio = idx_meio_subida
    while idx_inicio < idx_descida and derivada[idx_inicio] > 0.15 * pico_derivada:
        idx_inicio += 1
        
    idx_inicio += 2 
    idx_fim = idx_descida - 3 

    if idx_fim <= idx_inicio:
        idx_fim = len(sinal) - 1

    tempo_rec = tempo[idx_inicio:idx_fim]
    sinal_rec = sinal[idx_inicio:idx_fim]

    tempo_rec = tempo_rec - tempo_rec[0]

    return tempo_rec, sinal_rec

# =============================================================================
# 3. PARÂMETROS GEOMÉTRICOS
# =============================================================================

def calcular_parametros_geometricos(z, z_op, m):
    V = z / z_op
    num = 2 * m * V
    den_a = ((1 + 2*m)**2 + V**2)/2
    den_b = 1 + 2*m + V**2
    return num, den_a, den_b

# =============================================================================
# 4. MODELO SHEN
# =============================================================================

def modelo_shen_normalizado(t, theta, tc, num, den_a, den_b):
    t_safe = np.where(t <= 0, 1e-12, t)
    denominador = (den_a * (tc/(2*t_safe)) + den_b)
    argumento = num / denominador
    return (1 - (theta/2) * np.arctan(argumento))**2

# =============================================================================
# 5. AJUSTE
# =============================================================================

def ajustar_sinal_tl(tempo, sinal, num, den_a, den_b):
    
    I0 = np.mean(sinal[:10])
    sinal_norm = sinal / I0

    theta_guess = abs(np.mean(sinal_norm[-10:]) - sinal_norm[0])
    if theta_guess < 0.05:
        theta_guess = 0.5

    tc_guess = tempo[len(tempo)//4]
    if tc_guess <= 0:
        tc_guess = 1e-3

    p0 = [theta_guess, tc_guess]

    limites_inf = [0, 1e-7]
    limites_sup = [20, 10]

    func_fit = lambda t, theta, tc: modelo_shen_normalizado(t, theta, tc, num, den_a, den_b)

    popt, _ = curve_fit(func_fit, tempo, sinal_norm, p0=p0, bounds=(limites_inf, limites_sup), maxfev=30000)

    theta, tc = popt
    ajuste = func_fit(tempo, theta, tc)

    return theta, tc, ajuste, sinal_norm

# =============================================================================
# 6. DELTA T
# =============================================================================

def calcular_delta_T(theta, tc, tempo, lambda_ex, L, dndT):
    t = tempo[-1]
    k = np.arange(1,101)
    termo1 = (-2)**k
    termo2 = k * factorial(k+1)
    base = 1/(1 + 2*t/tc)
    termo3 = 1 - base**k
    
    soma = np.sum((termo1/termo2)*termo3)
    termo_log = np.log(1 + 2*t/tc)
    
    deltaT = -(theta * lambda_ex) / (4*np.pi*L*dndT) * (termo_log + soma)
    return deltaT

# =============================================================================
# 7. EFICIÊNCIA QUÂNTICA
# =============================================================================

def calcular_quantico(theta, P_abs, kappa, lambda_ex, dndT, lambda_em):
    phi = -(theta * kappa * lambda_ex) / (P_abs * dndT)
    eta = (1 - phi) * (lambda_em/lambda_ex)
    return phi, eta

# =============================================================================
# 8. MAIN
# =============================================================================

def main():

    diretorio = "/home/rodrigo/Área de Trabalho/studies/Python/Raspberry pi 3/PYQT/Versoes/V_3/DAQ/"

    tempo_bruto, sinal_bruto, nome = carregar_dados_reais(diretorio)
    tempo, sinal = isolar_pulso(tempo_bruto, sinal_bruto)

    # =========================================================
    # PARÂMETROS GEOMÉTRICOS 
    # =========================================================
    z_op = 1.02e-3
    z = -1.0e-3 
    m = 1.0

    num, den_a, den_b = calcular_parametros_geometricos(z, z_op, m)

    # =========================================================
    # PARÂMETROS FÍSICOS DA AMOSTRA
    # =========================================================
    L = 1e-3
    dndT = -3.94e-4
    kappa = 0.171
    P_in = 15.6e-3       # Potência bruta incidente medida pelo Power Meter
    A = 0.3567
    lambda_ex = 532e-9
    lambda_em = 560e-9

    # =========================================================
    # CÁLCULO DE PERDAS FIXAS (10%)
    # =========================================================
    perda_cubeta = 0.10
    T_parede_frontal = 1.0 - perda_cubeta
    
    # Potência que efetivamente entra no líquido
    P_in_real = P_in * T_parede_frontal

    # Potência absorvida pela amostra
    P_abs = P_in_real * (1 - 10**(-A))

    # =========================================================
    # AJUSTES E RESULTADOS
    # =========================================================
    theta, tc, ajuste, sinal_norm = ajustar_sinal_tl(tempo, sinal, num, den_a, den_b)

    deltaT = calcular_delta_T(theta, tc, tempo, lambda_ex, L, dndT)
    phi, eta = calcular_quantico(theta, P_abs, kappa, lambda_ex, dndT, lambda_em)

    print("\n===================================")
    print(f"ARQUIVO ANALISADO: {nome}")
    print("===================================")
    print(f"Perda Adotada (Cubeta): {perda_cubeta*100:.1f}%")
    print(f"Potência Útil no Líquido: {P_in_real*1000:.2f} mW")
    print("-----------------------------------")
    print(f"Theta (θ)     = {theta:.4f}")
    print(f"tc            = {tc*1000:.3f} ms")
    print(f"Delta T       = {deltaT:.3f} °C")
    print(f"phi           = {phi:.4f}")
    print(f"eta           = {eta:.4f}")
    print(f"eta (%)       = {eta*100:.2f} %")
    print("===================================\n")

    # Gráficos
    plt.figure(figsize=(8,5))
    plt.plot(tempo*1000, sinal_norm, 'b.', alpha=0.5, label='Experimental')
    plt.plot(tempo*1000, ajuste, 'r-', linewidth=2.5, label='Fit Shen')
    plt.xlabel("Tempo (ms)")
    plt.ylabel(r"$I(V,t)/I(V,0)$")
    plt.title("Thermal Lens Fit (Fase de Aquecimento Isolada)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    deltaT_temporal = ((ajuste - ajuste[0]) / (ajuste[-1] - ajuste[0])) * deltaT

    plt.figure(figsize=(8,5))
    plt.plot(tempo*1000, deltaT_temporal, 'k-', linewidth=2)
    plt.xlabel("Tempo (ms)")
    plt.ylabel(r"$\Delta T$ (°C)")
    plt.title("Evolução Temporal da Temperatura")
    plt.grid(True)
    plt.tight_layout()

    plt.show()

if __name__ == "__main__":
    main()