import urllib.request
import os, shutil
import zipfile

# class to manage the handling of files to scrape
class ManageFiles():
    def __init__(self, url):
        self.url = url
        self.file_name = url.split('/')[-1]
        self.directory = '/usr/src/app/upload/'
        self.zip_location = self.directory + 'zips/'
        self.working_dir = self.directory + 'temp/'
        
    # downloads companyhouse zip file to /app/upload/zips/    
    def download(self):
        with urllib.request.urlopen(self.url) as response, open(self.zip_location + self.file_name, 'wb') as out_file:
            data = response.read()
            out_file.write(data)

    # extacts the zip into  /app/upload/temp/
    def unzip(self):
        with zipfile.ZipFile(self.zip_location + self.file_name, 'r') as zip_ref:
            zip_ref.extractall(self.working_dir)

    # deletes all the files from /app/upload/temp/
    def delete(self):
        for filename in os.listdir(self.working_dir):
            file_path = os.path.join(self.working_dir, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
    
    # lists all the filenames in /app/upload/temp/
    def list_files(self):
        return os.listdir(self.working_dir)
