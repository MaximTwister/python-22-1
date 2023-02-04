from images_downloader import ImagesDownloader


def main():
    images = ImagesDownloader("config.ini")
    images.prepare_images_path()
    images.sync_download()

    images.set_directory_path("images-cat")
    images.prepare_images_path()
    images.set_theme("cat")
    images.get_list_images()
    images.async_download()


main()
