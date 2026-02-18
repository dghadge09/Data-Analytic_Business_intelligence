import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def create_healthcare_dq_architecture_diagram():
    fig, ax = plt.subplots(figsize=(20, 16), dpi=300)

    # Define colors
    colors = {
        'trigger': 'red',
        'process': 'teal',
        'validation': 'yellow',
        'database': 'green',
        'decision': 'pink',
        'action': 'darkpink',
        'external': 'purple'
    }

    # Create the diagram components
    components = {
        'Schedule Trigger': (0.5, 0.9, colors['trigger']),
        'ETL Path': (0.2, 0.7, colors['process']),
        'DQ Issue Tracking Path': (0.8, 0.7, colors['process']),
        'Validation Check (Missing Emails)': (0.2, 0.5, colors['validation']),
        'Validation Check (Suspicious Payments)': (0.2, 0.4, colors['validation']),
        'Logging Node': (0.5, 0.3, colors['action']),
        'Counting Node': (0.5, 0.2, colors['action']),
        'Decision Node': (0.5, 0.1, colors['decision']),
        'Alert Generation': (0.8, 0.1, colors['action']),
        'PostgreSQL Database': (0.5, 0.05, colors['database']),
        'External Services': (0.9, 0.05, colors['external'])
    }

    # Draw components in the diagram
    for component, (x, y, color) in components.items():
        ax.add_patch(mpatches.Rectangle((x - 0.1, y - 0.05), 0.2, 0.1, color=color, ec='black'))
        ax.text(x, y, component, ha='center', va='center', fontsize=12)

    # Add arrows to show flow
    ax.annotate('', xy=(0.5, 0.85), xytext=(0.5, 0.8), arrowprops=dict(arrowstyle='->', color='black'))
    ax.annotate('', xy=(0.2, 0.65), xytext=(0.2, 0.55), arrowprops=dict(arrowstyle='->', color='black'))
    ax.annotate('', xy=(0.8, 0.65), xytext=(0.8, 0.55), arrowprops=dict(arrowstyle='->', color='black'))
    
    # Set limits and title
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')  # Turn off the axis
    plt.title('Healthcare Data Quality Monitoring Architecture', fontsize=16)

    # Draw a legend
    legend_elements = [mpatches.Patch(color=color, label=key) for key, color in colors.items()]
    ax.legend(handles=legend_elements, loc='upper right')

    # Save the figure
    plt.savefig('Healthcare_DQ_Architecture_Diagram.png', bbox_inches='tight')
    plt.close()

create_healthcare_dq_architecture_diagram()