using System;
using Microsoft.Quantum.Simulation.Simulators;
using Microsoft.Quantum.Simulation.Core;

namespace QuantumChatbotDriver {
    class Driver {
        static void Main(string[] args) {
            using (var sim = new QuantumSimulator()) {
                // Chamar operação quântica
                var result = QuantumAnalysis.Run(sim, new double[] { }).Result;
                Console.WriteLine($"Resultado da análise quântica: {result}");
            }
        }
    }
}
