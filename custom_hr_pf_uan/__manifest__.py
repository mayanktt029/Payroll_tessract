{
    'name': 'HR Employee PF & UAN Fields',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Add PF Account No. and UAN No. to HR Employee & Date Of Joining And How much Time to work Employee in (Year, Month, Day)',
    'author': 'Mayank Prajapati',
    'description': "    To enhance the hr.employee form, we will integrate the PF Account Number and UAN Number fields within the HR Settings section, ensuring seamless access without adding extra tabs. We will also include a Date of Joining field, alongside an automated calculation of the employee's total service duration (displayed in years, months, and days) based on the joining date. This will provide a comprehensive view of each employee's tenure directly in the HR Settings section.",

    'depends': ['hr'],
    'data': [
        'views/hr_employee_view.xml',
    ],
    'installable': True,
    'application': False,
}
