## Projeto de Criptografia de Arquivos com AES-256-GCM
  Este projeto implementa um sistema simples e seguro de criptografia e descriptografia de arquivos, utilizando AES-256-GCM, um padrão criptográfico moderno e amplamente adotado em ambientes profissionais.
O foco não é apenas proteger o conteúdo do arquivo, mas também garantir que os metadados sejam criptografados, evitando vazamentos indiretos de informação. Nem todos sabem, mas arquivos(ex: .jpg, .png, .pdf, .docx...) podem carregar informações sensíveis nos metadados, como localização, data/hora, sistema operacional etc.

---

## Conceito-chave
Criptografia mal feita costuma falhar não no conteúdo, mas nos metadados.
Este projeto resolve esse problema ao criptografar os metadados junto com os dados, garantindo:
- Confidencialidade total;
- Integridade dos dados;
- Autenticidade do arquivo;
- Nada sensível fica em texto claro.

---

## 🔒 Algoritmos e padrões utilizados
- AES-256-GCM;
- Criptografia simétrica moderna;
- Garante confidencialidade + integridade, isto é, se o arquivo criptografado for modificado, a descriptografia vai falhar;
- Padrão profissional (NIST / uso industrial);
- Scrypt (KDF – Key Derivation Function);
- Deriva uma chave segura a partir de uma senha(Garantindo que o uso de CPU/memória e GPU seja impraticável);
- Resistente a ataques por força bruta e hardware especializado;
- Usa salt aleatório por arquivo, garantindo que chaves de deivação diferentes sejam geradas para a mesma senha. 

---

# O que é criptografado
Dentro do payload criptografado estão incluídos:
- Conteúdo completo do arquivo;
- Metadados:
  - Nome original do arquivo
  - Tamanho original (em bytes)
Esses metadados não ficam visíveis no arquivo .enc.

---

## Como usar
1. Criptografar um arquivo;
- Execute a célula de criptografia no notebook;
- Informe o caminho do arquivo;
- Informe a senha (guarde-a com cuidado);
- O arquivo será salvo como: arquivo_original.ext.enc.

---

2. Descriptografar um arquivo
- Execute a célula de descriptografia;
- Informe o caminho do arquivo .enc;
- Informe a senha correta;
- O arquivo original será restaurado com o nome original, conteúdo intacto e metadados recuperados.

---

## ⚠️ Observações importantes:
1. Perder a senha = perder o arquivo;
2. Não há recuperação sem a senha correta;
3. O projeto lê o arquivo inteiro em memória. Não é ideal para arquivos gigantes (isso pode ser aprimorado);
4. O foco é clareza, segurança e didática, não performance extrema.

---

## Objetivo do projeto
Este projeto foi desenvolvido com fins educacionais e práticos, demonstrando:
- Uso correto de AES-GCM;
- Uso consciente de KDFs;
- Importância da proteção de metadados;
- Boas práticas criptográficas aplicadas, não teóricas.
