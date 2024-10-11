
import numpy as np
from scipy.linalg import eigh_tridiagonal

def compute_energy_levels(Z_eff, num_levels=5, N=1000, r_max=20):
    # Physical Constants (SI Units)
    hbar = 1.0545718e-34       # Reduced Planck constant, J·s
    m_e = 9.10938356e-31       # Electron mass, kg
    m_p = 1.6726219e-27        # Proton mass, kg
    e = 1.602176634e-19         # Elementary charge, C
    epsilon_0 = 8.854187817e-12 # Vacuum permittivity, F/m
    pi = np.pi

    # Reduced Mass (mu)
    mu = m_e * m_p / (m_e + m_p)

    # Radial Grid
    r_min = 1e-12    # Avoid r=0
    a0 = 4 * pi * epsilon_0 * hbar**2 / (mu * e**2)
    r_max = r_max * a0  # Scaled by a0
    r = np.linspace(r_min, r_max, N)
    dr = r[1] - r[0]

    # Effective Coulomb Potential
    V_eff = -Z_eff * e**2 / (4 * pi * epsilon_0 * r)

    # Kinetic Energy Operator (Finite Difference)
    diag = np.full(N, 2.0) / dr**2 + (2 * mu / hbar**2) * V_eff
    off_diag = np.full(N-1, -1.0) / dr**2

    # Scaling factors
    diag *= (hbar**2) / (2 * mu)
    off_diag *= (hbar**2) / (2 * mu)

    # Solve the eigenvalue problem
    eigenvalues, eigenvectors = eigh_tridiagonal(diag, off_diag)

    # Convert energy eigenvalues from Joules to electron volts (eV)
    eV = 1.602176634e-19
    eigenvalues_eV = eigenvalues / eV

    # Select the first few energy levels
    selected_eigenvalues = eigenvalues_eV[:num_levels]
    selected_eigenvectors = eigenvectors[:, :num_levels]

    # Normalize the wavefunctions
    normalized_wavefunctions = []
    for n in range(num_levels):
        psi = selected_eigenvectors[:, n]
        probability_density = np.abs(psi)**2 * r**2
        norm = np.sqrt(np.sum(probability_density) * dr)
        psi_normalized = psi / norm
        normalized_wavefunctions.append(np.array2string(psi_normalized, precision=5, separator=','))
        # Alternatively, you can serialize as JSON or save to a file

    return selected_eigenvalues.tolist(), normalized_wavefunctions, (r / a0).tolist()
