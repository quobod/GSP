
class File:
    def __init__(this):
        this.name = ''
        this.path = ''
        this.ext = ''

    def getName(this):
        return this.name

    def getPath(this):
        return this.path

    def getExt(this):
        return this.ext

    def to_string(this):
        return this.path


class FileManager:
    def __inti__(this):
        this.files = dict()
