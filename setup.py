from distutils.core import setup

setup(
	name='nudibranch',  
    packages = ['nudibranch'],
	version='0.1',
	py_modules=['nudibranch'],
	author="David Dempsey",
	author_email="ddempsey786@gmail.com",
	description="Unnecessary matplotlib colormaps inspired by sea slugs.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	install_requires=['matplotlib'],
	url="https://github.com/ddempsey/nudibranch",
	download_url='https://github.com/ddempsey/nudibranch/archive/v_01.tar.gz',
	license='MIT',
	classifiers=[
		 "Programming Language :: Python :: 3",
		 "License :: OSI Approved :: MIT License",
		 "Operating System :: OS Independent",
	],
 )