#write functions here, don't add input('') statements here!

# Function to calculate the assessment value
def get_assessment_value(value):
    assessment_value = value * 0.60
    return assessment_value

# Function to calculate the property tax
def get_tax_assessed(assessment_value):
    tax_rate = 0.72  # $0.72 for each $100 of assessment value
    property_tax = (assessment_value / 100) * tax_rate
    return property_tax
