import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='lilendian',
     version='1.1',
     scripts=['lilendian'] ,
     author="phx",
     author_email="emai@example.com",
     description="A small program that simply returns escaped shell code in Little Endian format for whatever memory address you enter as the first argument.",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/phx/lilendian",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 2.7",
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
