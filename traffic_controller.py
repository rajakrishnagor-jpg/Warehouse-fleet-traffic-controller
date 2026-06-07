import random
import time

class WarehouseGrid:
    def __init__(self):
        # A simple 3x3 layout represented by barcodes
        self.grid_barcodes = {
            (0,0): "BC-A1", (0,1): "BC-A2", (0,2): "BC-A3",
            (1,0): "BC-B1", (1,1): "BC-B2", (1,2): "BC-B3",
            (2,0): "BC-C1", (2,1): "BC-C2", (2,2): "BC-C3"
        }
        self.blocked_barcodes = set()

    def monitor_network_latency(self):
        """Simulates edge diagnostics measuring TCP/IP latency in milliseconds"""
        # Simulate normal latency (10-30ms) with a 25% chance of a peak season spike (120-250ms)
        if random.random() < 0.25:
            latency = random.randint(120, 250)
        else:
            latency = random.randint(10, 30)
            
        print(f"📊 [EDGE DIAGNOSTICS] TCP/IP Latency: {latency}ms")
        
        # If latency exceeds the 100ms threshold, flag a network warning
        if latency > 100:
            print("⚠️  [NETWORK WARN] Latency spike detected! Potential heartbeat delay.")
        return latency

    def check_and_route(self, current_pos, target_pos, obstacle_detected=False):
        print(f"[SYSTEM INITIATED] Routing agent from {self.grid_barcodes[current_pos]} to {self.grid_barcodes[target_pos]}")
        
        # Check network health before calculating path
        self.monitor_network_latency()
        
        # If an edge sensor detects an obstacle along the planned path
        if obstacle_detected:
            failed_node = (1, 1) # Center node blocked
            failed_barcode = self.grid_barcodes[failed_node]
            self.blocked_barcodes.add(failed_barcode)
            
            print(f"🚨 [OBSTACLE DETECTED] Node {failed_node} is compromised.")
            print(f"❌ [ISOLATION] Flagging and Blocking Barcode: {failed_barcode}")
            print(f"🔄 [REROUTING] Recalculating alternative path bypassing {failed_barcode}...")
            
            # Simulated alternative edge path bypasses the center (1,1)
            alternative_path = [current_pos, (0,1), (0,2), target_pos]
            path_barcodes = [self.grid_barcodes[node] for node in alternative_path]
            print(f"✅ [SUCCESS] New Safe Path Found: {' -> '.join(path_barcodes)}\n")
        else:
            print("🚀 [SUCCESS] Path Clear. Standard trajectory executed successfully.\n")

if __name__ == "__main__":
    controller = WarehouseGrid()
    
    # Run 3 simulated missions to observe telemetry variations
    print("=== STARTING PEAK SEASON SIMULATION ===")
    for mission in range(1, 4):
        print(f"--- Executing Mission #{mission} ---")
        # Randomly inject an obstacle scenario on the second or third mission
        has_obstacle = (mission == 2)
        controller.check_and_route(current_pos=(1,0), target_pos=(1,2), obstacle_detected=has_obstacle)
        time.sleep(0.5) # Small delay between missions
        
    print(f"Final Global Blocked Barcode Registry: {list(controller.blocked_barcodes)}")
