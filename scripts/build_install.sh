rm -r build
rm -r dist

python setup.py bdist_wheel

pip install dist/*.whl --force-reinstall