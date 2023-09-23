class Image:
    """
    MasterBlaster Image Object

    :param imageType: The type of image
    :param imageId: The id of the image
    :param originalImageId: The id of the original image

    :ivar type: The type of image
    :ivar id: The id of the image
    :ivar original_id: The id of the original image
    """

    def __init__(self, imageType: int, imageId: str, originalImageId: str) -> None:
        self.type: int = imageType
        self.id: str = imageId
        self.original_id: str = originalImageId
