import matplotlib.pyplot as plt
import numpy as np

def draw_diagram():
    # Create a new figure
    plt.figure(figsize=(10, 8))
    
    # Add diagram nodes
    plt.scatter([0.5], [0.9], s=1000, color='lightblue', label='Healthcare Data Quality')
    plt.scatter([0.2, 0.8], [0.6, 0.6], s=800, color='lightgreen', label='Data Sources')
    plt.scatter([0.2, 0.8], [0.4, 0.4], s=800, color='yellow', label='Data Processing')
    plt.scatter([0.5], [0.2], s=1000, color='lightcoral', label='Data Quality Assessment')
    
    # Add text annotations
    plt.text(0.5, 0.9, 'Healthcare Data Quality', ha='center', va='center', fontsize=12)
    plt.text(0.2, 0.6, 'Electronic Health Records', ha='center', va='center', fontsize=10)
    plt.text(0.8, 0.6, 'Wearable Devices', ha='center', va='center', fontsize=10)
    plt.text(0.2, 0.4, 'Data Cleaning', ha='center', va='center', fontsize=10)
    plt.text(0.8, 0.4, 'Data Integration', ha='center', va='center', fontsize=10)
    plt.text(0.5, 0.2, 'Data Quality Metrics\nAccuracy, Completeness, Consistency', ha='center', va='center', fontsize=10)
    
    # Draw arrows
    plt.arrow(0.5, 0.9, -0.3, -0.3, head_width=0.05, head_length=0.05, fc='black', ec='black')
    plt.arrow(0.5, 0.9, 0.3, -0.3, head_width=0.05, head_length=0.05, fc='black', ec='black')
    plt.arrow(0.2, 0.6, 0, -0.2, head_width=0.05, head_length=0.05, fc='black', ec='black')
    plt.arrow(0.8, 0.6, 0, -0.2, head_width=0.05, head_length=0.05, fc='black', ec='black')

    # Set limits and remove axes
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.axis('off')
    
    # Save the diagram as PNG
    plt.savefig('healthcare_data_quality_diagram.png', format='png')
    plt.close()

if __name__ == "__main__":
    draw_diagram()