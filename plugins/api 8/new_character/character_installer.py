# ba_meta require api 8
# (see https://ballistica.net/wiki/meta-tag-system)

from __future__ import annotations

from typing import TYPE_CHECKING

import bascenev1 as bs
import bauiv1 as bui
import _babase
import os
import shutil
import hashlib
from bauiv1lib import popup

if TYPE_CHECKING:
	from typing import Any, Sequence


class Info:
	mod_dir = 'character_data'  # folder
	mod_name = 'character'  # name
	creator = 'SEBASTIAN2059' # creator
	url = '' # video

class Lang:
	lang = bs.app.lang.language
	if lang == 'Spanish':
		install_success = '¡Instalación Exitosa!'
		install_fail = '¡Instalación Fallida!'
		uninstall_success = '¡Desinstalación Exitosa!'
		uninstall_fail = '¡Desinstalación Fallida!'
		created = 'Creado por: ' + Info.creator
		title = 'Opciones del Mod'
		resources_text = 'Recursos: '
		resources_info = '¿No era lo que esperabas?.\nAgrega o elimina los archivos del mod.'
		install = 'Instalar'
		uninstall = 'Desinstalar'
	else:
		install_success = 'Installation Successful!'
		install_fail = 'Installation Failed!'
		uninstall_success = 'Uninstallation Successful!'
		uninstall_fail = 'Uninstallation Failed!'
		created = 'Created by: ' + Info.creator
		title = 'Mod Settings'
		resources_text = 'Resources: '
		resources_info = "Wasn't it what you expected?\nAdd or remove mod files."
		install = 'Install'
		uninstall = 'Uninstall'


class IntallPopup(popup.PopupWindow):

	def __init__(self, success: bool = True, unistall: bool = False):
		app = bui.app
		uiscale = app.ui.uiscale
		self._width = 400
		self._height = 310
		bg_color = (0.5, 0.4, 0.6)
		scale = (1.8 if uiscale is bui.UIScale.SMALL else
				 1.4 if uiscale is bui.UIScale.MEDIUM else 1.0)
		popup.PopupWindow.__init__(self,
								   position=(0.0, 0.0),
								   size=(self._width, self._height),
								   scale=scale,
								   bg_color=bg_color)

		mode = 'uninstall' if unistall else 'install'

		if mode == 'install' and success:
			install = Lang.install_success
			sound = 'achievement'
			image = 'chestOpenIcon'
			color = (0.0, 1.0, 0.0)
			modcolor = (1.0, 1.0, 1.0)
			extray = 0
		elif mode == 'install' and not success:
			install = Lang.install_fail
			sound = 'kronk2'
			image = 'chestIcon'
			color = (1.0, 0.1, 0.1)
			modcolor = (0.7, 0.7, 0.7)
			extray = -2
		elif mode == 'uninstall' and success:
			install = Lang.uninstall_success
			sound = 'achievement'
			image = 'chestOpenIcon'
			color = (0.0, 1.0, 0.0)
			modcolor = (1.0, 1.0, 1.0)
			extray = 0
		elif mode == 'uninstall' and not success:
			install = Lang.uninstall_fail
			sound = 'kronk2'
			image = 'chestIcon'
			color = (1.0, 0.1, 0.1)
			modcolor = (0.7, 0.7, 0.7)
			extray = -2

		save_button = btn = bui.buttonwidget(
			parent=self.root_widget,
			position=(self._width * 0.5 - 75, self._height * 0.07),
			size=(150, 52),
			scale=1.0,
			autoselect=True,
			color=(0.2, 0.8, 0.55),
			label=bui.Lstr(resource='okText'),
			on_activate_call=self.close
		)
		bui.textwidget(
			parent=self.root_widget,
			position=(self._width * 0.5, self._height * 0.9),
			size=(0, 0),
			h_align='center',
			v_align='center',
			scale=1.1,
			text=install,
			maxwidth=self._width * 0.7,
			color=color
		)
		bui.imagewidget(
			parent=self.root_widget,
			position=(self._width * 0.5 - 55, self._height * 0.494 + extray),
			size=(110, 110),
			texture=bui.gettexture(image)
		)
		bui.textwidget(
			parent=self.root_widget,
			position=(self._width * 0.5, self._height * 0.426),
			size=(0, 0),
			h_align='center',
			v_align='center',
			scale=1.3,
			text=Info.mod_name,
			maxwidth=self._width * 0.7,
			color=modcolor
		)
		bui.textwidget(
			parent=self.root_widget,
			position=(self._width * 0.5, self._height * 0.314),
			size=(0, 0),
			h_align='center',
			v_align='center',
			scale=0.8,
			text=Lang.created,
			maxwidth=self._width * 0.7,
			color=(1.0, 1.0, 0.0)
		)
		if not success:
			bs.getsound('error').play()
		bs.getsound(sound).play()

	def close(self) -> None:
		bui.containerwidget(
			edit=self.root_widget,
			transition='out_scale'
		)


class SettingsPopup(popup.PopupWindow):

	def __init__(self):
		uiscale = bui.app.ui_v1.uiscale
		self._transitioning_out = False
		self._width = 480
		self._height = 200
		bg_color = (0.4, 0.37, 0.49)

		# creates our _root_widget
		super().__init__(
			position=(0.0, 0.0),
			size=(self._width, self._height),
			scale=(
				2.06
				if uiscale is bui.UIScale.SMALL
				else 1.4
				if uiscale is bui.UIScale.MEDIUM
				else 1.0
			),
			bg_color=bg_color)

		self._cancel_button = bui.buttonwidget(
			parent=self.root_widget,
			position=(34, self._height - 48),
			size=(50, 50),
			scale=0.7,
			label='',
			color=bg_color,
			on_activate_call=self._on_cancel_press,
			autoselect=True,
			icon=bui.gettexture('crossOut'),
			iconscale=1.2)
		bui.containerwidget(edit=self.root_widget,
						   cancel_button=self._cancel_button)

		if Info.url != '':
			# YT?
			url_button = bui.buttonwidget(
				parent=self.root_widget,
				position=(self._width - 86, self._height - 51),
				size=(82, 82),
				scale=0.5,
				label='',
				color=(1.1, 0.0, 0.0),
				on_activate_call=self._open_url,
				autoselect=True,
				icon=bui.gettexture('startButton'),
				iconscale=1.73,
				icon_color=(1.3, 1.3, 1.3))

		title = bui.textwidget(
			parent=self.root_widget,
			position=(self._width * 0.49, self._height - 27 - 5),
			size=(0, 0),
			h_align='center',
			v_align='center',
			scale=1.0,
			text=Lang.title,
			maxwidth=self._width * 0.6,
			color=bui.app.ui_v1.title_color)

		self.cfgname = Info.mod_dir + Info.mod_name
		plugin_mode = bui.app.config[self.cfgname]

		v = + 50
		bui.textwidget(
			parent=self.root_widget,
			position=(self._width * 0.35, self._height * 0.8 - v),
			size=(0, 0),
			h_align='center',
			v_align='center',
			scale=1.0,
			text=Lang.resources_text,
			maxwidth=230,
			color=(0.8, 0.8, 0.8, 1.0),
		)
		popup.PopupMenu(
			parent=self.root_widget,
			position=(self._width * 0.5, self._height * 0.68 - v),
			width=150,
			choices=['install', 'uninstall'],
			choices_display=[
				bui.Lstr(value=Lang.install),
				bui.Lstr(value=Lang.uninstall),
			],
			current_choice=plugin_mode['resources'],
			on_value_change_call=self._set_mode,
		)
		v += 50
		info = bui.textwidget(
			parent=self.root_widget,
			position=(self._width * 0.49, self._height * 0.75 - v),
			size=(0, 0),
			h_align='center',
			v_align='center',
			scale=1.0,
			text=Lang.resources_info,
			maxwidth=self._width * 0.6,
			color=bui.app.ui_v1.title_color)
		

	def _set_mode(self, val: str) -> None:
		cfg = bui.app.config
		cfg[self.cfgname]['resources'] = val
		cfg.apply_and_commit()

	def _open_url(self) -> None:
		bui.open_url(Info.url)

	def _on_cancel_press(self) -> None:
		self._transition_out()

	def _transition_out(self) -> None:
		if not self._transitioning_out:
			self._transitioning_out = True
			bui.containerwidget(edit=self.root_widget, transition='out_scale')

	def on_popup_cancel(self) -> None:
		bui.getsound('swish').play()
		self._transition_out()


class Installer:

	def __init__(self) -> None:
		self.python_user = _babase.env()["python_directory_user"]
		self.files_dir = self.python_user + '/' + Info.mod_dir + '/'
		self.app_dir = _babase.env()["python_directory_app"] + '/'
		self.data_dir = self.app_dir + '../'
		self.models_dir = self.data_dir + 'meshes/'
		self.audios_dir = self.data_dir + 'audio/'
		self.textures_dir = self.data_dir + 'textures/'
		self.platform = _babase.app.classic.platform
		self.audios: list = []
		self.models: list = []
		self.textures: list = []
		self.get_mod()

	def get_mod(self) -> None:
		fls = os.listdir(self.files_dir)
		for fl in fls:
			if fl.endswith('.ogg'): # audio
				self.audios.append(fl)
			if fl.endswith('.bob') or fl.endswith('.cob'): # models
				self.models.append(fl)
			if fl.endswith('.ktx') or fl.endswith('.dds'): # textures
				self.textures.append(fl)

	@staticmethod
	def check_file_same(f1, f2):
		try:
			md5s = [hashlib.md5(), hashlib.md5()]
			fs = [f1, f2]
			for i in range(2):
				f = open(fs[i], 'rb')
				block_size = 2 ** 20
				while True:
					data = f.read(block_size)
					if not data: break
					md5s[i].update(data)
				f.close()
				md5s[i] = md5s[i].hexdigest()
			return md5s[0] == md5s[1]
		except Exception as e:
			return False

	def _installed(self) -> None:
		installed = True
		for a in self.audios:
			app = self.audios_dir + a
			user = self.files_dir + a
			if not os.path.isfile(app):
				installed = False
				break
			if not self.check_file_same(app, user):
				installed = False
				break
		for m in self.models:
			app = self.models_dir + m
			user = self.files_dir + m
			if not os.path.isfile(app):
				installed = False
				break
			if not self.check_file_same(app, user):
				installed = False
				break
		for t in self.textures:
			if self.platform == 'android':
				if t.endswith('.dds'):
					continue
			else:
				if t.endswith('.ktx'):
					continue
			app = self.textures_dir + t
			user = self.files_dir + t
			if not os.path.isfile(app):
				installed = False
				break
			if not self.check_file_same(app, user):
				installed = False
				break
		return installed

	def install_mod(self) -> None:
		if self._installed():
			return
		try:
			for a in self.audios:
				app = self.audios_dir + a
				user = self.files_dir + a
				shutil.copyfile(user, app)
			for m in self.models:
				app = self.models_dir + m
				user = self.files_dir + m
				print(app)
				print(user)
				print(self.python_user)
				shutil.copyfile(user, app)
			for t in self.textures:
				if self.platform == 'android':
					if t.endswith('.dds'):
						continue
				else:
					if t.endswith('.ktx'):
						continue
				app = self.textures_dir + t
				user = self.files_dir + t
				shutil.copyfile(user, app)
			bui.timer(1.0, bui.Call(IntallPopup, True))
		except:
			bui.timer(1.0, bui.Call(IntallPopup, False))

	def uninstall_mod(self) -> None:
		if not self._installed():
			return
		try:
			for a in self.audios:
				app = self.audios_dir + a
				os.remove(app)
			for m in self.models:
				app = self.models_dir + m
				os.remove(app)
			for t in self.textures:
				if self.platform == 'android':
					if t.endswith('.dds'):
						continue
				else:
					if t.endswith('.ktx'):
						continue
				app = self.textures_dir + t
				os.remove(app)
			bui.timer(1.0, bui.Call(IntallPopup, True, True))
		except:
			bui.timer(1.0, bui.Call(IntallPopup, False, True))

# ba_meta export plugin
class Character(bs.Plugin):

	def on_app_running(self) -> None:
		self.setup_config()

	def setup_config(self) -> None:
		cfgname = Info.mod_dir + Info.mod_name
		if not cfgname in bs.app.config:
			mod_list = {
				'resources': 'install',
			}
			bs.app.config[cfgname] = mod_list
			bs.app.config.apply_and_commit()
		plugin_mode = bs.app.config[cfgname]
		if plugin_mode['resources'] == 'install':
			Installer().install_mod()
			if Installer()._installed():
				exec('import ' + Info.mod_dir + '.register_appearance')
		else:
			Installer().uninstall_mod()

	def has_settings_ui(self) -> bool:
		return True

	def show_settings_ui(self, source_widget: bui.Widget | None) -> None:
		SettingsPopup()
