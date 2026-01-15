# Script para criar arquivos de classes do Dragão Brasil
# Extrai conteúdo do full_text.txt e cria arquivos markdown estruturados

$sourceFile = "c:\jogos\backup\backup\ddddd\accessible-tormenta\extracted\dragao-brasil\full_text.txt"
$outputDir = "c:\jogos\backup\backup\ddddd\accessible-tormenta\livros\dragao-brasil\02-classes"

# Ler todo o conteúdo do arquivo fonte
$fullText = Get-Content $sourceFile -Raw -Encoding UTF8

# Função para extrair seção entre linhas
function Extract-Section {
    param(
        [string]$Text,
        [int]$StartLine,
        [int]$EndLine
    )
    
    $lines = $Text -split "`n"
    $section = $lines[($StartLine-1)..($EndLine-1)] -join "`n"
    return $section
}

# Função para criar arquivo de classe
function Create-ClassFile {
    param(
        [string]$FileName,
        [string]$Title,
        [string]$Content,
        [string]$Previous,
        [string]$Next
    )
    
    $filePath = Join-Path $outputDir $FileName
    
    $header = @"
---
title: "$Title"
book: "dragao-brasil"
chapter: "02-classes"
---

# $Title

"@

    $footer = @"

---

[← Anterior: $Previous]($Previous) | [Próximo: $Next →]($Next)
"@

    $fullContent = $header + $Content + $footer
    
    Set-Content -Path $filePath -Value $fullContent -Encoding UTF8
    Write-Host "✓ Criado: $FileName" -ForegroundColor Green
}

Write-Host "`n=== Criando arquivos de classes ===" -ForegroundColor Cyan

# Ler linhas do arquivo
$lines = Get-Content $sourceFile -Encoding UTF8

# Extrair seções de classe (exemplo - você pode ajustar conforme necessário)
$barbaroContent = ($lines[1503..1571] | Out-String)
$bardoContent = ($lines[1571..1649] | Out-String)
$bucaneiro = ($lines[1649..1725] | Out-String)
$cacador = ($lines[1725..1862] | Out-String)
$cavaleiro = ($lines[1792..1862] | Out-String)
$druida = ($lines[1862..2193] | Out-String)
$guerreiro = ($lines[2193..2274] | Out-String)
$inventor = ($lines[2193..2349] | Out-String)
$ladino = ($lines[2274..2422] | Out-String)
$lutador = ($lines[2349..2501] | Out-String)
$miragem = ($lines[2422..2579] | Out-String)
$mistico = ($lines[2579..3062] | Out-String)
$nobre = ($lines[2998..3062] | Out-String)
$samurai = ($lines[3062..3513] | Out-String)

# Criar arquivos
Create-ClassFile "02-barbaro.md" "Bárbaro" $barbaroContent "01-arcanista.md" "03-bardo.md"
Create-ClassFile "03-bardo.md" "Bardo" $bardoContent "02-barbaro.md" "04-bucaneiro.md"
Create-ClassFile "04-bucaneiro.md" "Bucaneiro" $bucaneiro "03-bardo.md" "05-cacador.md"
Create-ClassFile "05-cacador.md" "Caçador" $cacador "04-bucaneiro.md" "06-cavaleiro.md"
Create-ClassFile "06-cavaleiro.md" "Cavaleiro" $cavaleiro "05-cacador.md" "07-druida.md"
Create-ClassFile "07-druida.md" "Druida" $druida "06-cavaleiro.md" "08-guerreiro.md"
Create-ClassFile "08-guerreiro.md" "Guerreiro" $guerreiro "07-druida.md" "09-inventor.md"
Create-ClassFile "09-inventor.md" "Inventor" $inventor "08-guerreiro.md" "10-ladino.md"
Create-ClassFile "10-ladino.md" "Ladino" $ladino "09-inventor.md" "11-lutador.md"
Create-ClassFile "11-lutador.md" "Lutador" $lutador "10-ladino.md" "12-miragem.md"
Create-ClassFile "12-miragem.md" "Miragem" $miragem "11-lutador.md" "13-mistico.md"
Create-ClassFile "13-mistico.md" "Místico" $mistico "12-miragem.md" "14-nobre.md"
Create-ClassFile "14-nobre.md" "Nobre" $nobre "13-mistico.md" "15-samurai.md"
Create-ClassFile "15-samurai.md" "Samurai" $samurai "14-nobre.md" "README.md"

Write-Host "`n=== Concluído! ===" -ForegroundColor Green
Write-Host "14 arquivos de classes criados em: $outputDir" -ForegroundColor Yellow
