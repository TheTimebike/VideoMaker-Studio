# -*- mode: python -*-

block_cipher = None


a = Analysis(['Main.py'],
             pathex=['C:\\Users\\Callum\\Desktop\\VideoMaker\\VideoMaker-Studio'],
             binaries=[],
             datas=[("praw.ini", "."),("vms.ico", ".")],
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
          exclude_binaries=True,
          name='Main',
          debug=False,
          strip=False,
          upx=True,
          console=False,
          icon='vms.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='Main')
