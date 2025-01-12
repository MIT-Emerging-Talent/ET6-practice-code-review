#include <iostream>
#include <thread>
#include <chrono> // For delays

using namespace std;

void trafficLightSimulation() {
    while (true) {
        // Red Light
        cout << "🔴 Red Light ON" << endl;
        this_thread::sleep_for(chrono::seconds(5)); // Wait for 5 seconds

        // Green Light
        cout << "🟢 Green Light ON" << endl;
        this_thread::sleep_for(chrono::seconds(5)); // Wait for 5 seconds

        // Yellow Light
        cout << "🟡 Yellow Light ON" << endl;
        this_thread::sleep_for(chrono::seconds(2)); // Wait for 2 seconds

        cout << endl; // Add space before restarting the cycle
    }
}

int main() {
    cout << "Starting Traffic Light Simulation..." << endl;
    trafficLightSimulation();
    return 0;
}
