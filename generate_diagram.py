import matplotlib.pyplot as plt

# Function to generate the Healthcare Data Quality Architecture diagram
def generate_diagram():
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Sample data for the diagram (customize as necessary)
    ax.text(0.5, 0.9, 'Healthcare Data Quality Architecture', fontsize=15, ha='center')
    
    # Example components of the architecture (customize as necessary)
    ax.text(0.5, 0.7, 'Data Sources', fontsize=12, ha='center')
    ax.text(0.5, 0.5, 'Data Integration', fontsize=12, ha='center')
    ax.text(0.5, 0.3, 'Data Analysis', fontsize=12, ha='center')
    ax.text(0.5, 0.1, 'Data Governance', fontsize=12, ha='center')
    
    # Draw separating lines (for visual clarity)
    ax.hlines([0.8, 0.6, 0.4, 0.2], 0.15, 0.85, colors='gray', linestyles='dashed')
    
    ax.axis('off')  # Hide axes
    plt.title('Healthcare Data Quality Architecture', fontsize=14)
    plt.savefig('healthcare_data_quality_architecture.png')  # Save as PNG
    plt.close()

if __name__ == '__main__':
    generate_diagram()