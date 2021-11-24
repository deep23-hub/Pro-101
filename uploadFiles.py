import dropbox

class TransferData:
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A84jiC1ppziBFGpqd9wS1-SnxnP7ykglUyeYR6FgRw-q7-gr1w182QSSIQcFL0rWftrLNINXH6GvS_rkn6pMFtaAzYOG3g-TLdmnZoutdKOMKDrCUmAQH-hoj93RUQsiIWnpgKA'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()