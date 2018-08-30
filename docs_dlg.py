"""
My first Gui :)

docs_dlg app to download docs from readthedocs website
Provide the Exect title of the document

"""

import wget
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MainWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title='My New Gtk App')
		self.set_default_size(400,100)
		self.set_border_width(10)

		#main layout
		self.layout = Gtk.Box(spacing = 10, orientation=Gtk.Orientation.VERTICAL)
		grid = Gtk.Grid()
		self.add(self.layout)
		self.add(grid)
		#Boxes
		entry_box = Gtk.Box(spacing = 10)
		dl_box = Gtk.Box(spacing = 10)


		# Entry Field (Label & Box & get title text)
		self.label = Gtk.Label("Please Enter The exact Doc title ")
		self.entry_field = Gtk.Entry()

		self.save_to_bttn = Gtk.Button("SELECT FOLDER")
		self.save_to_bttn.connect("clicked", self.clicked_save_to_bttn)

		self.get_bttn = Gtk.Button("Download!")
		self.get_bttn.connect("clicked", self.clicked_get_bttn)

		entry_box.add(self.label)
		entry_box.add(self.entry_field)
		entry_box.add(self.save_to_bttn)
		entry_box.add(self.get_bttn)

		
		#Informing Label
		self.label_finish = Gtk.Label()


		#add all to the layout
		self.layout.pack_start(entry_box, False, False, 0)
		self.layout.add(self.label_finish)

	def clicked_save_to_bttn(self, widget):
		self.title = self.entry_field.get_text()


		path = Gtk.FileChooserDialog("Choose the path", self, Gtk.FileChooserAction.SELECT_FOLDER, (
			Gtk.STOCK_OPEN, Gtk.ResponseType.OK,
			Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
		))

		resp = path.run()

		if resp == Gtk.ResponseType.OK:
			self.selected_path = str(path.get_current_folder())

		elif resp == Gtk.ResponseType.CANCEL:
			return

		path.destroy()

	def clicked_get_bttn(self, widget):
		create_url = self.get_URL(self.title)
		doc_dl = self.download_the_doc(create_url, out=self.selected_path)
		if doc_dl :
			self.label_finish.set_markup("<b> FINISHED </b>")

	def get_URL(self, doc_title):
		url_main = 'http://media.readthedocs.org/pdf/{}/latest/{}.pdf'.format(doc_title, doc_title)
		print('doc_url = %s' % url_main)
		return url_main

	def download_the_doc(self, get_URL, out=None):
		print('Downloading your doc...\n')
		wget.download(get_URL, out)
		return True


win = MainWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()


