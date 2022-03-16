import tarfile

tar = tarfile.open('model.tar.gz')
tar.extractall('./extract')
tar.close()