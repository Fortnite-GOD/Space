# -*- mode: python -*-

block_cipher = None


a = Analysis(['space-war-1.py'],
             pathex=['C:\\Users\\cdunla6940\\Documents\\Computer Programming\\space'],
             binaries=[],
             datas=[("Images", "Images"),
                    ("Sounds", "Sounds"),
                    ("Fonts", "Fonts")
                    ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Ian Hawke Revenge',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
