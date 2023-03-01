from edgedriver_autoinstaller.utils import get_edge_version, download_edgedriver

def test_get_edge_version():
    version = get_edge_version()
    assert version is None or version.count('.') == 3

def test_download_edgedriver():
    assert download_edgedriver(True) is not None
    