import uuid


def get_product_image_upload_folder(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{str(uuid.uuid4())}.{ext}"
    return "/".join(["images", instance.branch.name, "products", filename])