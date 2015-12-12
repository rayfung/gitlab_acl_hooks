#!/usr/bin/env python3

acl_dict = dict()
acl_dict['rayfung'] = dict(default='pass')
acl_dict['guotao']  = dict(default='pass')
acl_dict['hui']     = dict(default='deny', pass_pattern=r'^Assets/Effects_Enemy/.+|^Assets/Models/Character/.+\.fbx\.meta$')
