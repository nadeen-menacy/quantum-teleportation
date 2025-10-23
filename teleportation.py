from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.execute_function import execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


# Step 1: Create circuit (3 qubits, 3 classical bits)
qc = QuantumCircuit(3, 3)

# Step 2: Prepare the unknown state on qubit 0
qc.h(0)  # Creates superposition: |ψ⟩ = (|0⟩ + |1⟩)/√2

# Step 3: Create an entangled pair between qubits 1 and 2 (Alice and Bob)
qc.h(1)
qc.cx(1, 2)
qc.barrier()

# Step 4: Perform Bell measurement on Alice’s qubits (0 and 1)
qc.cx(0, 1)
qc.h(0)
qc.measure([0, 1], [0, 1])
qc.barrier()

# Step 5: Apply conditional operations based on measurement results
qc.cx(1, 2)
qc.cz(0, 2)

# Step 6: Measure Bob’s qubit to verify teleportation
qc.measure(2, 2)

# Draw circuit
qc.draw("mpl")
plt.show()

# Step 7: Simulate
backend = Aer.get_backend("qasm_simulator")
result = execute(qc, backend, shots=1024).result()
counts = result.get_counts()

# Plot histogram
plot_histogram(counts)
plt.show()
