from registry import registry

# ผู้ใช้เพิ่ม logic เองได้โดยไม่ต้องแก้ core

def custom_api(data):
    return {
        "custom": True,
        "input": data
    }

registry.register("custom_api", custom_api)
