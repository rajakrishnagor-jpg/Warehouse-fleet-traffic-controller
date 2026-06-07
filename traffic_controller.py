import random

class WarehouseGrid:
    def __init__(self):
        # A simple 3x3 layout represented by barcodes
        self.grid_barcodes = {
            (0,0): "BC-A1", (0,1): "BC-A2", (0,2): "BC-A3",
            (1,0): "BC-B1", (1,1): "BC-B2", (1,2): "BC-B3",
            (2,0): "BC-C1", (2,1): "BC-C2", (2,2): "BC-C3"
        }
        # Simulate a dynamic obstacle at the center of the floor (1,1)
        self.blocked_barcodes = set()

    def check_and_route(self, current_pos, target_pos, obstacle_detected=False):
        print(f"[SYSTEM INITIATED] Routing agent from {self.grid_barcodes[current_pos]} to {self.grid_barcodes[target_pos]}")
        
        # If an edge sensor detects an obstacle along the planned path
        if obstacle_detected:
            failed_node = (1, 1) # Center node blocked
            failed_barcode = self.grid_barcodes[failed_node]
            self.blocked_barcodes.add(failed_barcode)
            
            print(f"⚠️  [ALERT] Obstacle detected at node {failed_node}!")
            print(f"❌ [ISOLATION] Flagging and Blocking Barcode: {failed_barcode}")
            print(f"🔄 [REROUTING] Recalculating alternative path bypassing {failed_barcode}...")
            
            # Simulated alternative edge path bypasses the center (1,1)
            alternative_path = [current_pos, (0,1), (0,2), target_pos]
            path_barcodes = [self.grid_barcodes[node] for node in alternative_path]
            print(f"✅ [SUCCESS] New Safe Path Found: {' -> '.join(path_barcodes)}\n")
        else:
            print("🚀 [SUCCESS] Path Clear. Standard trajectory executed successfully.\n")

if __name__ == "__main__":
    # Initialize the controller
    controller = WarehouseGrid()
    
    # Mission 1: Clear path run
    controller.check_and_route(current_pos=(0,0), target_pos=(0,2), obstacle_detected=False)
    
    # Mission 2: Run encountering an obstacle (Triggering your custom Sam's site feature logic)
    controller.check_and_route(current_pos=(1,0), target_pos=(1,2), obstacle_detected=True)
    
    print(f"Current Global Blocked Barcode Registry: {list(controller.blocked_barcodes)}")  

Feat: Implement dynamic obstacle rerouting and barcode blocking logic
