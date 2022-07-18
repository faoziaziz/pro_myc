# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['voicebot-mycroft.py'],
             pathex=['.'],
             binaries=[('/usr/lib/x86_64-linux-gnu/libxcb.so.1','.')],
             datas=[],
             hiddenimports=['_portaudio'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='voicebot-mycroft',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='voicebot-mycroft')

