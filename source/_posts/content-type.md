---
title: Content-Type参考手册
date: 2018-02-24 20:52:37
categories:
  - 其他
---

### 介绍

web开发者对于响应头(Response Headers)中Content-Type肯定不会陌生。
一个http请求返回时，浏览器可以通过Content-Type判断返回的资源属于哪种MIME Type媒体类型，从而决定如何响应该资源。
但实际上，Content-Type并不一定要严格遵守，浏览器会在一些情况下会自行处理。

所有的MIME Type，也即所有的Content-Type可能情况，可以通过[一个官方的媒体类型清单][official]查看到。 该清单由IANA维护着，它是制定MIME Type的权威机构。

下面会根据资源的媒体类型，给出一个比较常见的MIME Type对照表。其中有两个最主要的类型:
- text/plain 是文本文件的默认值。文本文件应当是人类可读的，不包含二进制数据。
- application/octet-stream 是所有非文本的默认值。有未知的文件类型时就可以使用此类型。浏览器在处理该类型文件时会特别小心。


**文本** :

| Extension  |  Kind of document  | MIME Type   |
|:-----------|:------------------|:-------------|
|  .css  |    Cascading Style Sheets (CSS)  | text/css  |
|  .js   |    JavaScript   |  text/javascript，推荐使用application/javascript  |
|  .htm .html |  HyperText Markup Language (HTML)  |  text/html   |
|  .xml  |   Extensible Markup Language (XML)   |  text/xml，也可以使用application/xml  |
|  .csv  |    Comma-separated values (CSV)  | text/csv    |
|  .ics  |    iCalendar format  | text/calendar    |
|  .md   |    markdown          | text/markdown  |
|  .rtf  |    Rich Text Format  | text/rtf       |


**图片** :

| Extension  |  Kind of document  | MIME Type   |
|:-----------|:------------------|:-------------|
|  .bmp    |   位图              |   image/bmp     |
|  .gif  |    Graphics Interchange Format (GIF)    |  image/gif    |
|  .jpeg .jpg  |    JPEG images   |   image/jpeg   |
|  .png  |    Portable Network Graphics  |  image/png    |
|  .svg  |    Scalable Vector Graphics (SVG)  | image/svg+xml    |
|  .tiff |    Tagged Image File Format (TIFF)  | image/tiff    |
|  .webp |    WEBP image  | image/webp    |


**视频** :

| Extension  |  Kind of document  | MIME Type   |
|:-----------|:------------------|:-------------|
|  .avi  |   AVI: Audio Video Interleave   |  video/x-msvideo  |
|  .mp4  |    mp4 format                   |   video/mp4       |
|  .mov  |    quicktime                    |   video/quicktime |
|  .mpeg |    MPEG Video  | video/mpeg     |
|  .ogv  |    OGG video   | video/ogg      |
|  .webm |    WEBM video  | video/webm     |
|  .3gp  |    3GPP audio/video container   | video/3gpp，不包含视频时为 audio/3gpp    |
|  .3g2  |    3GPP2 audio/video container  | video/3gpp2，不包含视频时为 audio/3gpp2  |


**音频** :

| Extension  |  Kind of document  | MIME Type   |
|:-----------|:------------------|:-------------|
|  .aac  |    AAC audio          |  audio/aac    |
|  .mid .midi |  Musical Instrument Digital Interface (MIDI)  | audio/midi   |
|  .oga  |    OGG audio          |  audio/ogg    |
|  .wav  | Waveform Audio Format |  audio/wav    |
|  .weba |     WEBM audio        |  audio/webm   |


**字体** :

| Extension  |  Kind of document  | MIME Type   |
|:-----------|:------------------|:-------------|
|  .otf  |    OpenType font  | font/otf    |
|  .ttf  |    TrueType Font  | font/ttf    |
|  .woff |    Web Open Font Format (WOFF) |  font/woff    |
|  .woff2|    Web Open Font Format (WOFF) |  font/woff2   |


**微软系列产品**, 属于**application**的一部分:

| Extension  |  Kind of document  | MIME Type   |
|:-----------|:------------------|:-------------|
| .doc    |  | application/msword  |
| .dot    |  | application/msword  |
| .docx   |  Microsoft Office Word 2007 document     |  application/vnd.openxmlformats-officedocument.wordprocessingml.document  |
| .docm   |  Office Word 2007 macro-enabled document |  application/vnd.ms-word.document.macroEnabled.12 |
| .dotx   |  Office Word 2007 template    |  application/vnd.openxmlformats-officedocument.wordprocessingml.template  |
| .dotm   |  Office Word 2007 macro-enabled document template  | application/vnd.ms-word.template.macroEnabled.12  |
| .xls    |  |  application/vnd.ms-excel  |
| .xlt    |  |  application/vnd.ms-excel  |
| .xla    |  |  application/vnd.ms-excel  |
| .xlsx   |  Microsoft Office Excel 2007 workbook  | application/vnd.openxmlformats-officedocument.spreadsheetml.sheet  |
| .xlsm   |  Office Excel 2007 macro-enabled workbook  | application/vnd.ms-excel.sheet.macroEnabled.12  | 
| .xltx   |  Office Excel 2007 template   | application/vnd.openxmlformats-officedocument.spreadsheetml.template  |
| .xltm   |  Office Excel 2007 macro-enabled workbook template  | application/vnd.ms-excel.template.macroEnabled.12  |
| .xlsb   |  Office Excel 2007 binary workbook  |  application/vnd.ms-excel.sheet.binary.macroEnabled.12  |
| .xlam   |  Office Excel 2007 add-in  | application/vnd.ms-excel.addin.macroEnabled.12  |
| .ppt    |  |   application/vnd.ms-powerpoint  |
| .pot    |  |   application/vnd.ms-powerpoint  |
| .pps    |  |   application/vnd.ms-powerpoint  |
| .ppa    |  |   application/vnd.ms-powerpoint  |
| .pptx   |  Microsoft Office PowerPoint 2007 presentation  | application/vnd.openxmlformats-officedocument.presentationml.presentation |
| .pptm   |  Office PowerPoint 2007 macro-enabled presentation |  application/vnd.ms-powerpoint.presentation.macroEnabled.12  |
| .ppsx   |  Office PowerPoint 2007 slide show  | application/vnd.openxmlformats-officedocument.presentationml.slideshow  |
| .ppsm   |  Office PowerPoint 2007 macro-enabled slide show  | application/vnd.ms-powerpoint.slideshow.macroEnabled.12  |
| .potx   |  Office PowerPoint 2007 template | application/vnd.openxmlformats-officedocument.presentationml.template |
| .potm   |  Office PowerPoint 2007 macro-enabled presentation template  | application/vnd.ms-powerpoint.template.macroEnabled.12  |
| .ppam   |  Office PowerPoint 2007 add-in  | application/vnd.ms-powerpoint.addin.macroEnabled.12  |
| .sldx   |  Office PowerPoint 2007 slide  | application/vnd.openxmlformats-officedocument.presentationml.slide  |
| .sldm   |  Office PowerPoint 2007 macro-enabled slide  | application/vnd.ms-powerpoint.slide.macroEnabled.12   |
| .one    |  Microsoft Office OneNote 2007 section   | application/msonenote  |
| .onetoc2|  Office OneNote 2007 TOC   | application/msonenote  |
| .onetmp |  Office OneNote 2007 temporary file  | application/msonenote  |
| .onepkg |  Office OneNote 2007 package   | application/msonenote  |
| .thmx   |  2007 Office system release theme  | application/vnd.ms-officetheme  |
| .mdb    |  Office Access  |  application/vnd.ms-access  |


**其他application类型** :

| Extension  |  Kind of document  | MIME Type   |
|:-----------|:------------------|:-------------|
|  .azw  |    Amazon Kindle eBook format    | application/vnd.amazon.ebook    |
|  .mpkg |    Apple Installer Package       | application/vnd.apple.installer+xml    |
|  .abw  |    AbiWord document  | application/x-abiword    |
|  .odt  |    OpenDocument text document    | application/vnd.oasis.opendocument.text    |
|  .odp  |    OpenDocument presentation document |  application/vnd.oasis.opendocument.presentation    |
|  .ods  |    OpenDocument spreadsheet document  |  application/vnd.oasis.opendocument.spreadsheet    |
|  .arc  |    Archive document (multiple files embedded)   |  application/octet-stream    |
|  .bin  |    Any kind of binary data       | application/octet-stream        |
|  .epub |    Electronic publication (EPUB) |  application/epub+zip    |
|  .es   |    ECMAScript (IANA Specification)    |  application/ecmascript    |
|  .js   |    JavaScript   |  application/javascript    |
|  .json |    JSON format  |  application/json   |
|  .pdf  |    Adobe Portable Document Format (PDF)  | application/pdf    |
|  .rtf  |    Rich Text Format (RTF)  |  application/rtf    |
|  .sh   |   Bourne shell script  | application/x-sh    |
|  .swf  |    Small web format (SWF) or Adobe Flash document  |  application/x-shockwave-flash    |
|  .xhtml|      XHTML  | application/xhtml+xml    |
|  .xml  |      XML    | application/xml    |
|  .jar  |    Java Archive (JAR)  | application/java-archive    |
|  .rar  |    RAR archive         | application/x-rar-compressed    |
|  .tar  |    Tape Archive (TAR)  | application/x-tar    |
|  .zip  |    ZIP archive         | application/zip    |
|  .7z   |   7-zip archive        | application/x-7z-compressed    |
|  .bz   |    BZip archive        | application/x-bzip     |
|  .bz2  |    BZip2 archive       | application/x-bzip2    |
  
### 参考链接

* [Official MIME Types][official]
* [Microsoft TechNet][office-2007]
* [MDN Web Docs][mozilla]

[official]: http://www.iana.org/assignments/media-types/media-types.xhtml
[office-2007]: https://technet.microsoft.com/en-us/library/ee309278(office.12).aspx
[mozilla]: https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Complete_list_of_MIME_types
