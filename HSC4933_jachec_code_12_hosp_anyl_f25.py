############################################################################
# Author         : Harrison Jachec                                         #
# Date           : December 6 2025                                         #
# Arguments      : HSC4933_jachec_code_10_hosp_anyl_f25.py                 #
# Description    : Hospital patient satisfaction and readmission analysis. #
# Email          : harrisonjachec@usf.edu                                  #
############################################################################

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


def read_patient_data(filename):
    """
    Read patient data from a text file and return a DataFrame.
    
    Parameters:
    filename (str): Path to the patient data file
    
    Returns:
    pd.DataFrame: DataFrame containing patient information
    """
    try:
        # Initialize lists for storing parsed data
        patient_ids = []
        readmissions = []
        staff_sat = []
        cleanliness_sat = []
        food_sat = []
        comfort_sat = []
        communication_sat = []
        
        # Open and read the file
        with open(filename, 'r') as file:
            lines = file.readlines()
            
            # Skip header row
            for line in lines[1:]:
                try:
                    values = [v.strip() for v in line.split(',')]
                    
                    # Validate that we have the correct number of fields
                    if len(values) != 7:
                        print(f"Warning: Line has incorrect number of fields: {line.strip()}")
                        continue
                    
                    patient_ids.append(int(values[0]))
                    readmissions.append(int(values[1]))
                    staff_sat.append(int(values[2]))
                    cleanliness_sat.append(int(values[3]))
                    food_sat.append(int(values[4]))
                    comfort_sat.append(int(values[5]))
                    communication_sat.append(int(values[6]))
                    
                except ValueError as e:
                    print(f"Error parsing line: {line.strip()} - {str(e)}")
                    continue
        
        # Create DataFrame
        df = pd.DataFrame({
            'PatientID': patient_ids,
            'Readmission': readmissions,
            'StaffSatisfaction': staff_sat,
            'CleanlinessSatisfaction': cleanliness_sat,
            'FoodSatisfaction': food_sat,
            'ComfortSatisfaction': comfort_sat,
            'CommunicationSatisfaction': communication_sat
        })
        
        if len(df) == 0:
            raise ValueError("No valid data found in the file")
        
        return df
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        return None


def calculate_statistics(df):
    """
    Calculate and display basic statistics from patient data.
    
    Parameters:
    df (pd.DataFrame): Patient data DataFrame
    
    Returns:
    dict: Dictionary containing calculated statistics
    """
    stats = {
        'total_patients': len(df),
        'num_readmitted': df['Readmission'].sum(),
        'readmission_rate': (df['Readmission'].sum() / len(df)) * 100,
        'avg_staff': df['StaffSatisfaction'].mean(),
        'avg_cleanliness': df['CleanlinessSatisfaction'].mean(),
        'avg_food': df['FoodSatisfaction'].mean(),
        'avg_comfort': df['ComfortSatisfaction'].mean(),
        'avg_communication': df['CommunicationSatisfaction'].mean()
    }
    
    return stats


def display_statistics(stats):
    """
    Display calculated statistics in a formatted manner.
    
    Parameters:
    stats (dict): Dictionary of statistics
    """
    print("=" * 60)
    print("HOSPITAL PATIENT DATA ANALYSIS")
    print("=" * 60)
    print(f"\nNumber of Patients Analyzed: {stats['total_patients']}")
    print(f"Number of Patients Readmitted: {stats['num_readmitted']}")
    print(f"Readmission Rate: {stats['readmission_rate']:.2f}%")
    
    print("\n" + "=" * 60)
    print("AVERAGE SATISFACTION SCORES BY CATEGORY")
    print("=" * 60)
    print(f"Average Staff Satisfaction: {stats['avg_staff']:.2f}")
    print(f"Average Cleanliness Satisfaction: {stats['avg_cleanliness']:.2f}")
    print(f"Average Food Satisfaction: {stats['avg_food']:.2f}")
    print(f"Average Comfort Satisfaction: {stats['avg_comfort']:.2f}")
    print(f"Average Communication Satisfaction: {stats['avg_communication']:.2f}")


def calculate_overall_satisfaction(df):
    """
    Calculate overall satisfaction score for each patient.
    
    Parameters:
    df (pd.DataFrame): Patient data DataFrame
    
    Returns:
    pd.DataFrame: DataFrame with added OverallSatisfaction column
    """
    df['OverallSatisfaction'] = (df['StaffSatisfaction'] + 
                                  df['CleanlinessSatisfaction'] + 
                                  df['FoodSatisfaction'] + 
                                  df['ComfortSatisfaction'] + 
                                  df['CommunicationSatisfaction']) / 5
    
    print(f"\nAverage Overall Satisfaction: {df['OverallSatisfaction'].mean():.2f}")
    
    return df


def perform_logistic_regression(df):
    """
    Perform logistic regression to analyze correlation between satisfaction and readmission.
    
    Parameters:
    df (pd.DataFrame): Patient data DataFrame with OverallSatisfaction column
    
    Returns:
    dict: Dictionary containing regression results and the fitted model
    """
    # Prepare data
    X = df[['OverallSatisfaction']].values
    y = df['Readmission'].values
    
    # Create and fit model
    log_reg = LogisticRegression()
    log_reg.fit(X, y)
    
    # Get predictions and probabilities
    y_pred = log_reg.predict(X)
    y_pred_proba = log_reg.predict_proba(X)[:, 1]
    
    # Calculate metrics
    accuracy = (y_pred == y).mean()
    auc_score = roc_auc_score(y, y_pred_proba)
    
    # Interpret correlation
    coefficient = log_reg.coef_[0][0]
    
    if abs(coefficient) < 0.1:
        correlation_strength = "Very Weak"
    elif abs(coefficient) < 0.3:
        correlation_strength = "Weak"
    elif abs(coefficient) < 0.7:
        correlation_strength = "Moderate"
    else:
        correlation_strength = "Strong"
    
    direction = "negative" if coefficient < 0 else "positive"
    
    results = {
        'model': log_reg,
        'coefficient': coefficient,
        'intercept': log_reg.intercept_[0],
        'accuracy': accuracy,
        'auc_score': auc_score,
        'correlation_strength': correlation_strength,
        'direction': direction,
        'y_pred': y_pred,
        'y_pred_proba': y_pred_proba,
        'y_actual': y
    }
    
    return results


def display_regression_results(results):
    """
    Display logistic regression results in a formatted manner.
    
    Parameters:
    results (dict): Dictionary of regression results
    """
    print("\n" + "=" * 60)
    print("LOGISTIC REGRESSION RESULTS")
    print("=" * 60)
    print(f"\nCoefficient (Beta): {results['coefficient']:.4f}")
    print(f"Intercept (Alpha): {results['intercept']:.4f}")
    print(f"Model Accuracy: {results['accuracy']:.4f}")
    print(f"AUC-ROC Score: {results['auc_score']:.4f}")
    
    print("\nInterpretation:")
    print(f"Correlation Strength: {results['correlation_strength']} {results['direction']} correlation")
    print(f"Interpretation: For every unit increase in overall satisfaction,")
    print(f"the odds of readmission change by a factor of {np.exp(results['coefficient']):.4f}")
    
    if results['coefficient'] < 0:
        print(f"\nThis suggests that HIGHER satisfaction scores are associated with")
        print(f"LOWER readmission rates, which is a positive finding.")
    else:
        print(f"\nThis suggests that HIGHER satisfaction scores are associated with")
        print(f"HIGHER readmission rates.")
    
    print("\n" + "=" * 60)
    print("CLASSIFICATION REPORT")
    print("=" * 60)
    print(classification_report(results['y_actual'], results['y_pred'], 
                                target_names=['No Readmission', 'Readmission']))
    
    print("\nConfusion Matrix:")
    cm = confusion_matrix(results['y_actual'], results['y_pred'])
    print(f"True Negatives: {cm[0, 0]}, False Positives: {cm[0, 1]}")
    print(f"False Negatives: {cm[1, 0]}, True Positives: {cm[1, 1]}")


def plot_logistic_regression(df, results):
    """
    Plot the logistic regression curve along with data points.
    
    Parameters:
    df (pd.DataFrame): Patient data DataFrame
    results (dict): Dictionary of regression results
    """
    # Prepare data
    X = df[['OverallSatisfaction']].values.flatten()
    y = df['Readmission'].values
    
    # Create figure
    plt.figure(figsize=(10, 6))
    
    # Plot actual data points
    readmitted = X[y == 1]
    not_readmitted = X[y == 0]
    
    plt.scatter(not_readmitted, [0]*len(not_readmitted), color='blue', 
               label='No Readmission', alpha=0.6, s=100)
    plt.scatter(readmitted, [1]*len(readmitted), color='red', 
               label='Readmission', alpha=0.6, s=100)
    
    # Plot regression curve
    x_range = np.linspace(X.min() - 0.1, X.max() + 0.1, 300)
    y_proba = results['model'].predict_proba(x_range.reshape(-1, 1))[:, 1]
    
    plt.plot(x_range, y_proba, 'g-', linewidth=2, label='Logistic Regression Curve')
    
    # Formatting
    plt.xlabel('Overall Satisfaction Score', fontsize=12, fontweight='bold')
    plt.ylabel('Probability of Readmission', fontsize=12, fontweight='bold')
    plt.title('Logistic Regression: Overall Satisfaction vs. Readmission Rate', 
             fontsize=14, fontweight='bold')
    plt.legend(loc='best')
    plt.grid(True, alpha=0.3)
    plt.ylim(-0.1, 1.1)
    
    # Add text box with model info
    textstr = f'Coefficient: {results["coefficient"]:.4f}\nAUC-ROC: {results["auc_score"]:.4f}'
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)
    plt.text(0.02, 0.98, textstr, transform=plt.gca().transAxes, fontsize=10,
            verticalalignment='top', bbox=props)
    
    plt.tight_layout()
    plt.savefig('logistic_regression_plot.png', dpi=300, bbox_inches='tight')
    print("\nPlot saved as 'logistic_regression_plot.png'")
    plt.show()


def main(filename='Week14Assignment.txt'):
    """
    Main function to run the hospital data analysis.
    
    Parameters:
    filename (str): Path to the patient data file
    """
    # Read data
    df = read_patient_data(filename)
    
    if df is None:
        return
    
    # Calculate and display basic statistics
    stats = calculate_statistics(df)
    display_statistics(stats)
    
    # Calculate overall satisfaction
    df = calculate_overall_satisfaction(df)
    
    # Perform logistic regression
    results = perform_logistic_regression(df)
    
    # Display regression results
    display_regression_results(results)
    
    # Plot the results
    plot_logistic_regression(df, results)
    
    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
