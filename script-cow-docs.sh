for f in "${formas[@]}"; do                             
cat << EOF > "${f}.md"
(${f})=

# ${f}

Comando: \`echo "Estou no formato ${f}" | cowsay -f ${f}\`

'''{literalinclude} saidas/${f}.txt 
'''

EOF
done

sed -i "s/'''/\`\`\`/g" docs/*.md
