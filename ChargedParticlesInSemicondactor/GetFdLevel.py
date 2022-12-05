from ChargedParticlesInSemicondactor.DonorFermiLevel import *

def calc_donor_fermi_levels() -> None:
    # поиск урвня Ферми для доноров
    result = calculate_charges(me=0.36, mh=0.36, t=300, Efpl=0.57, Efneg=1.12, Ec=1.12, Ev=0, Nd=1e16)
    print(result)
    result = calculate_charges(me=0.36, mh=0.36, t=300, Efpl=0.57, Efneg=1.12, Ec=1.12, Ev=0, Nd=2 * 1e16)
    print(result)
    result = calculate_charges(me=0.36, mh=0.36, t=300, Efpl=0.57, Efneg=1.12, Ec=1.12, Ev=0, Nd=4 * 1e16)
    print(result)
    result = calculate_charges(me=0.36, mh=0.36, t=300, Efpl=0.57, Efneg=1.12, Ec=1.12, Ev=0, Nd=8 * 1e16)
    print(result)
    result = calculate_charges(me=0.36, mh=0.36, t=300, Efpl=0.57, Efneg=1.12, Ec=1.12, Ev=0, Nd=1e17)
    print(result)
    result = calculate_charges(me=0.36, mh=0.36, t=300, Efpl=0.57, Efneg=1.12, Ec=1.12, Ev=0, Nd=2 * 1e17)
    print(result)
    result = calculate_charges(me=0.36, mh=0.36, t=300, Efpl=0.57, Efneg=1.12, Ec=1.12, Ev=0, Nd=4 * 1e17)
    print(result)
    result = calculate_charges(me=0.36, mh=0.36, t=300, Efpl=0.57, Efneg=1.12, Ec=1.12, Ev=0, Nd=8 * 1e17)
    print(result)
    result = calculate_charges(me=0.36, mh=0.36, t=300, Efpl=0.57, Efneg=1.12, Ec=1.12, Ev=0, Nd=1e18)
    print(result)
    result = calculate_charges(me=0.36, mh=0.36, t=300, Efpl=0.57, Efneg=1.12, Ec=1.12, Ev=0, Nd=2 * 1e18)
    print(result)
    result = calculate_charges(me=0.36, mh=0.36, t=300, Efpl=0.57, Efneg=1.12, Ec=1.12, Ev=0, Nd=4 * 1e18)
    print(result)
    result = calculate_charges(me=0.36, mh=0.36, t=300, Efpl=0.57, Efneg=1.12, Ec=1.12, Ev=0, Nd=8 * 1e18)
    print(result)
    result = calculate_charges(me=0.36, mh=0.36, t=300, Efpl=0.57, Efneg=1.12, Ec=1.12, Ev=0, Nd=1e19)
    print(result)