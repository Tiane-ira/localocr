# -*- mode: python ; coding: utf-8 -*-
from pathlib import Path

import rapidocr_onnxruntime
import onnxruntime

package_name = 'rapidocr_onnxruntime'
package_name2 = 'onnxruntime'
install_dir = Path(rapidocr_onnxruntime.__file__).resolve().parent
install_dir2 = Path(onnxruntime.__file__).resolve().parent

onnx_paths = list(install_dir.rglob('*.onnx'))
yaml_paths = list(install_dir.rglob('*.yaml'))
dll_paths = list(install_dir2.rglob('*.dll'))

onnx_add_data = [(str(v.parent), f'{package_name}/{v.parent.name}')
                 for v in onnx_paths]

dll_add_data = [(str(v), f'{package_name2}/{v.parent.name}')
                 for v in dll_paths]

yaml_add_data = []
for v in yaml_paths:
    if package_name == v.parent.name:
        yaml_add_data.append((str(v.parent / '*.yaml'), package_name))
    else:
        yaml_add_data.append(
            (str(v.parent / '*.yaml'), f'{package_name}/{v.parent.name}'))

add_data = list(set(yaml_add_data + onnx_add_data + dll_add_data))

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=add_data,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='rapidocr',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
