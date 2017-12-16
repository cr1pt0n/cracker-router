if [[ $EUID -ne 0 ]]; then
	echo -e "ESTE SCRIPT DEVE SER EXECUTADO COM PERMISSÕES ROOT \n"

exit 1
fi

echo "INSTALANDO AS DEPENDENCIAS"

pip install requests
pip install argparse
