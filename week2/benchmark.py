import boto3
import time
import os


filename = "submission.csv"
n_samples = 100


def benchmark_s3():
    upload_times = []
    download_times = []

    session = boto3.Session(profile_name="854407906105_HASANAccess")
    s3 = session.client("s3")

    bucket = "hasan-sangmin"
    key = filename
    for _ in range(n_samples):
        start = time.time()
        s3.upload_file(filename, bucket, key)
        elapsed_time = time.time() - start
        print(f"Upload: {elapsed_time} seconds")
        upload_times.append(elapsed_time)

    for _ in range(n_samples):
        start = time.time()
        s3.download_file(bucket, key, filename)
        elapsed_time = time.time() - start
        print(f"Download: {elapsed_time} seconds")
        download_times.append(elapsed_time)

    print(f"Average Upload time: {sum(upload_times) / n_samples}")
    print(f"Average Download time: {sum(download_times) / n_samples}")


def benchmark_ebs():
    upload_times = []
    download_times = []

    ebs_mount = "../"
    for _ in range(n_samples):
        start = time.time()
        with open(filename, "rb") as f_src:
            with open(os.path.join(ebs_mount, filename), "wb") as f_dst:
                f_dst.write(f_src.read())
        elapsed_time = time.time() - start
        print(f"Upload: {elapsed_time} seconds")

    for _ in range(n_samples):
        start = time.time()
        with open(os.path.join(ebs_mount, filename), "rb") as f_src:
            with open(filename, "wb") as f_dst:
                f_dst.write(f_src.read())
        elapsed_time = time.time() - start
        print(f"Download: {elapsed_time} seconds")

    print(f"Average Upload time: {sum(upload_times) / n_samples}")
    print(f"Average Download time: {sum(download_times) / n_samples}")


def benchmark_efs():
    upload_times = []
    download_times = []

    efs_mount = "~/efs"
    for _ in range(n_samples):
        start = time.time()
        with open(filename, "rb") as f_src:
            with open(os.path.join(efs_mount, filename), "wb") as f_dst:
                f_dst.write(f_src.read())
        elapsed_time = time.time() - start
        print(f"Upload: {elapsed_time} seconds")

    for _ in range(n_samples):
        start = time.time()
        with open(os.path.join(efs_mount, filename), "rb") as f_src:
            with open(filename, "wb") as f_dst:
                f_dst.write(f_src.read())
        elapsed_time = time.time() - start
        print(f"Download: {elapsed_time} seconds")

    print(f"Average Upload time: {sum(upload_times) / n_samples}")
    print(f"Average Download time: {sum(download_times) / n_samples}")


if __name__ == "__main__":
    benchmark_s3()
    benchmark_ebs()
    benchmark_efs()
