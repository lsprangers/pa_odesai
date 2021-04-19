#! kaggle datasets download -d open-source-sports/baseball-databank -p mmm_baseball/data/kaggle_data
#
# import kaggle
from pathlib import Path
import zipfile


class UnzipKaggleDatasetFiles:
    def __init__(self, zip_files, zip_direc, unzip_path):
        self.zip_files = zip_files
        self.zip_direc = zip_direc
        self.unzip_path = unzip_path

    def get_the_data_now(self):
        for zip_f in self.zip_files:
            zip_fpath = self.zip_direc / zip_f
            with zipfile.ZipFile(zip_fpath, 'r') as zip_ref:
                zip_ref.extractall(self.unzip_path)
            print(f"unzipped {zip_f} to {self.unzip_path}")


print(__name__)
print(__file__)

if __name__ == '__main__':
    baseball_dataset_zip_files = ("baseball-databank.zip", "the-history-of-baseball.zip")
    zip_dir = Path(Path.cwd() / "mmm_baseball/data/kaggle_data_zipfiles/")
    unzip_dir = Path(Path.cwd() / "mmm_baseball/data/kaggle_datasets/")

    kaggle_unzip = UnzipKaggleDatasetFiles(
        zip_files=baseball_dataset_zip_files,
        zip_direc=zip_dir,
        unzip_path=unzip_dir,
    )

    kaggle_unzip.get_the_data_now()
