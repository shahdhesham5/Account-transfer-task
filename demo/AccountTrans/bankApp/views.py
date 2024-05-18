from django.shortcuts import render,redirect
from .models import Account
from .resources import AccountResource
from django.contrib import messages
from tablib import Dataset
import csv,io


#uploading accounts data CSV file to django model
def upload(request):
    if request.method == 'POST':  # Check if the request method is POST
        account_resource = AccountResource()  # Instance of the resource class
        dataset = Dataset()  # Instance of Dataset from tablib to handle data
        new_file = request.FILES['myfile']  # Try to upload file using POST method

        if not new_file.name.endswith('csv'):  # Check if the file format is CSV
            messages.warning(request, 'Please upload a CSV file only.')
            return redirect('home')

        data_set = new_file.read().decode('UTF-8')  # Decode the file content
        io_string = io.StringIO(data_set)  # Create an io.StringIO object to work with CSV data
        next(io_string)  # Skip the first row assuming that it's the header

        # Iterate to create or update objects for each row in the CSV file
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            created = Account.objects.update_or_create(
            Identifier=column[0],
            name=column[1],
            balance=column[2],
            )
        
        messages.success(request, 'File uploaded successfully!')  # Set success message
        return redirect('home')
    
    return render(request, 'home.html')  # Render the home template if GET request






# Display all accounts.
def accounts(request):
    accounts = Account.objects.all()
    return render(request,'accounts.html',{'accounts':accounts})
