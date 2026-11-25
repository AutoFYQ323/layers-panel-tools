# -*- coding: utf-8 -*-
"""Sentences added after the 1.0.3 catalog.

Keys must match a tr() literal exactly, including newlines. This folder is
skipped by the Chinese-literal scan, so the keys live here on purpose.
"""


def _rows():
    rows = []

    def add(zh, en, es, fr, ar):
        rows.append((zh, en, es, fr, ar))

    add(
        "勾选多个矢量图层，选文件夹与格式，按图层名各导出一份。导出完成后会说明写到了哪里。勾选「合并为一个文件」时改为选择一个保存路径：GeoPackage、SQLite、KML、GML 一个文件多层；KMZ 写成一个 .kmz；Excel 和 ODS 一个工作簿一层一个表；CSV 再多一个「并成同一个表」，默认不勾，这时因为 CSV 不能有多个工作表，会写成同名的 Excel 文件，每个图层一个表，表名是图层名；勾上之后并进同一个 CSV 表，同名字段只出现一次，每个图层的字段都会保留，并加一列记下原来的图层名；DXF 也会合成一个文件，但会丢掉大部分属性。",
        "Check vector layers, pick a folder and a format, and export one file per layer name. When it finishes, a dialog says where the files went. When “Merge into one file” is checked, you choose one save path instead: GeoPackage, SQLite, KML, and GML keep one layer each inside that file; KMZ is written as one .kmz; Excel and ODS use one sheet per layer. CSV adds “One table”, off by default: CSV cannot hold several sheets, so the same name is written as an Excel file, one sheet per layer, named after the layer. When that box is on, every feature goes into one CSV table; a field name shared by several layers appears once, every layer’s own fields are kept, and a column records the source layer name. DXF is also combined into one file, but most attributes are dropped.",
        "Marca capas vectoriales, elige carpeta y formato, y exporta un archivo por nombre de capa. Al terminar, un cuadro dice dónde quedaron. Si marcas «Unir en un archivo», eliges una ruta de guardado: GeoPackage, SQLite, KML y GML guardan una capa cada una dentro de ese archivo; KMZ se escribe como un .kmz; Excel y ODS usan una hoja por capa. CSV añade «Una sola tabla», desmarcada por defecto: CSV no puede tener varias hojas, así que se escribe un Excel con el mismo nombre, una hoja por capa y con el nombre de la capa. Si se marca, todas las entidades van a una tabla CSV; un campo con el mismo nombre aparece una sola vez, no falta ningún campo de ninguna capa, y una columna guarda el nombre de la capa de origen. DXF también se junta en un solo archivo, pero pierde la mayoría de los atributos.",
        "Cochez des couches vectorielles, choisissez un dossier et un format, et exportez un fichier par nom de couche. À la fin, une boîte indique où les fichiers ont été écrits. Si « Fusionner en un fichier » est coché, vous choisissez un chemin d’enregistrement : GeoPackage, SQLite, KML et GML gardent une couche chacun dans ce fichier ; le KMZ est écrit en un .kmz ; Excel et ODS utilisent une feuille par couche. Le CSV ajoute « Une seule table », décochée par défaut : un CSV ne peut pas avoir plusieurs feuilles, donc le même nom est écrit en Excel, une feuille par couche, nommée comme la couche. Si la case est cochée, toutes les entités vont dans une table CSV ; un nom de champ commun n’apparaît qu’une fois, aucun champ d’aucune couche n’est perdu, et une colonne retient le nom de la couche d’origine. Le DXF est aussi regroupé en un seul fichier, mais la plupart des attributs sont perdus.",
        "حدد طبقات متجهة واختر مجلدًا وتنسيقًا، ويُصدَّر ملف لكل اسم طبقة. عند الانتهاء تظهر رسالة بمكان الملفات. عند تحديد «دمج في ملف واحد» تختار مسار الحفظ: GeoPackage وSQLite وKML وGML يحتفظ كل منها بطبقة داخل ذلك الملف؛ ويُكتب KMZ كملف ‎.kmz واحد؛ وExcel وODS يستخدمان ورقة لكل طبقة. يضيف CSV خيار «جدول واحد»، وهو غير محدد افتراضيًا: CSV لا يحتمل عدة أوراق، فيُكتب ملف Excel بالاسم نفسه، ورقة لكل طبقة باسم الطبقة. عند تحديده تذهب كل المعالم إلى جدول CSV واحد؛ اسم الحقل المشترك يظهر مرة واحدة، ولا يُسقط أي حقل من أي طبقة، ويُضاف عمود باسم الطبقة الأصلية. ويُجمع DXF أيضًا في ملف واحد، لكن معظم السمات تُسقط.",
    )
    add(
        "五项都作用在当前工程。清空数据会删除全部矢量图层的全部要素，图层还在，删掉后不能恢复。打开编辑、保存关闭针对所有矢量图层，做成了不弹框，失败才说明。复制到空、复制图层只针对当前选中的那一个图层，样式跟着走。复制到空不含要素，复制图层连要素一起复制。复制前会说明图层、路径和原格式。清空和复制做成了也会弹出。",
        "All five actions work on the current project. Clear data deletes every feature in every vector layer. The layers stay, and the deletion cannot be undone. Start editing and Save and close apply to every vector layer; success stays quiet, and only a failure is reported. Copy empty and Copy layer apply only to the one selected layer, and the style comes along. Copy empty has no features. Copy layer copies the features too. Before copying, the dialog names the layer, the path, and the original format. Clear data and the two copy actions still report when they succeed.",
        "Las cinco acciones actúan sobre el proyecto actual. Vaciar datos borra todas las entidades de todas las capas vectoriales. Las capas siguen ahí y lo borrado no se puede recuperar. Abrir edición y Guardar y cerrar valen para todas las capas vectoriales; si salen bien no avisan, y solo avisan si fallan. Copiar vacío y Copiar capa solo afectan a la capa seleccionada, y el estilo las acompaña. Copiar vacío no incluye entidades. Copiar capa copia también las entidades. Antes de copiar se indican la capa, la ruta y el formato original. Vaciar datos y las dos copias sí avisan cuando terminan.",
        "Les cinq actions portent sur le projet en cours. Vider les données supprime toutes les entités de toutes les couches vectorielles. Les couches restent, et la suppression est irréversible. Ouvrir l’édition et Enregistrer et fermer s’appliquent à toutes les couches vectorielles ; une réussite reste silencieuse, seul un échec est signalé. Copier à vide et Copier la couche ne visent que la couche sélectionnée, et le style suit. Copier à vide n’a pas d’entités. Copier la couche copie aussi les entités. Avant la copie, la boîte indique la couche, le chemin et le format d’origine. Vider les données et les deux copies signalent aussi leur réussite.",
        "الإجراءات الخمسة تعمل على المشروع الحالي. مسح البيانات يحذف كل المعالم في كل الطبقات المتجهة. الطبقات تبقى، والحذف لا يُسترجع. فتح التحرير وحفظ وإغلاق يشملان كل الطبقات المتجهة؛ النجاح بلا رسالة، والفشل فقط يُبلَّغ. النسخ فارغًا ونسخ الطبقة يقتصران على الطبقة المحددة، والنمط يتبعها. النسخ فارغًا بلا معالم. نسخ الطبقة ينسخ المعالم أيضًا. قبل النسخ تُذكر الطبقة والمسار والتنسيق الأصلي. مسح البيانات وعمليتا النسخ تظهر نتيجتهما عند النجاح أيضًا.",
    )
    add(
        "在当前选中的线两端标出起点和终点，并显示长度（米）。不写入图层，也不换掉选线工具。小窗可以拖动。开/关控制标注。展开后列出所选线，取消勾选会同时取消 QGIS 里的选中。最多标前 80 条。关掉小窗即停止。",
        "Mark the start and end of each selected line and show the length in meters. Nothing is written to the layer, and the line-selection tool stays as it is. The small window can be dragged. On/off controls the marks. When expanded, it lists the selected lines; clearing a check also clears that feature in QGIS. At most the first 80 lines are marked. Closing the window stops it.",
        "Marca el inicio y el final de cada línea seleccionada y muestra la longitud en metros. No escribe en la capa ni cambia la herramienta de selección de líneas. La ventanita se puede arrastrar. Activar/desactivar controla las marcas. Al desplegar, lista las líneas elegidas; quitar la casilla también quita la selección en QGIS. Como máximo se marcan las 80 primeras. Cerrar la ventana lo detiene.",
        "Marquez le début et la fin de chaque ligne sélectionnée et affichez la longueur en mètres. Rien n’est écrit dans la couche, et l’outil de sélection de lignes reste en place. La petite fenêtre se déplace. Marche/arrêt commande les marques. Une fois dépliée, elle liste les lignes choisies ; décocher retire aussi la sélection dans QGIS. Au plus les 80 premières lignes sont marquées. Fermer la fenêtre arrête tout.",
        "يضع علامة على بداية ونهاية كل خط محدد ويعرض الطول بالأمتار. لا يكتب في الطبقة ولا يستبدل أداة تحديد الخطوط. النافذة الصغيرة تُسحب. تشغيل/إيقاف يتحكم بالعلامات. عند الفتح تُسرد الخطوط المختارة، وإلغاء التحديد يلغي التحديد في QGIS أيضًا. يُعلَّم أول 80 خطًا على الأكثر. إغلاق النافذة يوقفه.",
    )
    add(
        "选择一个图层，按类写成多个文件，默认存到工程所在文件夹，格式默认是 ESRI 形状文件。分类图层默认按图例里的分类、分级或规则；普通图层默认按字段，每个不同的值一个文件。下拉框里分类图层用粗体红色标出，并显示要素个数。超过上限会跳过并说明。",
        "Choose one layer and write one file per class, by default into the project folder, in ESRI Shapefile. A classified layer starts from its categories, ranges, or rules. An ordinary layer starts from a field, one file per distinct value. Classified layers are shown in bold red in the list, with the feature count. Above the limit, the export stops and says why.",
        "Elige una capa y escribe un archivo por clase, por defecto en la carpeta del proyecto y en ESRI Shapefile. Una capa clasificada empieza por sus categorías, intervalos o reglas. Una capa normal empieza por un campo, un archivo por valor distinto. Las capas clasificadas salen en negrita roja en la lista, con el número de entidades. Por encima del tope, la exportación se detiene y explica por qué.",
        "Choisissez une couche et écrivez un fichier par classe, par défaut dans le dossier du projet, au format ESRI Shapefile. Une couche classée part de ses catégories, paliers ou règles. Une couche ordinaire part d’un champ, un fichier par valeur distincte. Les couches classées apparaissent en gras rouge dans la liste, avec le nombre d’entités. Au-dessus du plafond, l’export s’arrête et dit pourquoi.",
        "اختر طبقة واحدة واكتب ملفًا لكل فئة، افتراضيًا في مجلد المشروع وبتنسيق ESRI Shapefile. الطبقة المصنفة تبدأ من فئاتها أو نطاقاتها أو قواعدها. الطبقة العادية تبدأ من حقل، ملف لكل قيمة مختلفة. الطبقات المصنفة تظهر بالأحمر العريض في القائمة، مع عدد المعالم. إذا تجاوز العدد الحد يتوقف التصدير ويذكر السبب.",
    )
    add("分类导出", "Export by class", "Exportar por clase", "Exporter par classe", "تصدير حسب الفئة")
    add(
        "按图例分类或按字段，把一个图层拆成多个文件",
        "Split one layer into several files by legend class or by field",
        "Parte una capa en varios archivos por clase de leyenda o por campo",
        "Découpe une couche en plusieurs fichiers par classe de légende ou par champ",
        "يقسم طبقة واحدة إلى عدة ملفات حسب فئة المفتاح أو حسب الحقل",
    )
    add(
        "选择一个图层。分类图层默认按图例，普通图层默认按字段。每一类或每个不同的值写成一个文件。",
        "Choose one layer. A classified layer starts on the legend; an ordinary layer starts on a field. Each class, or each distinct value, becomes one file.",
        "Elige una capa. Una capa clasificada empieza por la leyenda; una capa normal empieza por un campo. Cada clase, o cada valor distinto, es un archivo.",
        "Choisissez une couche. Une couche classée commence par la légende ; une couche ordinaire commence par un champ. Chaque classe, ou chaque valeur distincte, devient un fichier.",
        "اختر طبقة واحدة. الطبقة المصنفة تبدأ من المفتاح، والطبقة العادية تبدأ من حقل. كل فئة، أو كل قيمة مختلفة، تصبح ملفًا.",
    )
    add("按图例分类", "By legend", "Por leyenda", "Par légende", "حسب المفتاح")
    add("按字段", "By field", "Por campo", "Par champ", "حسب الحقل")
    add("每层最多", "Max per layer", "Máximo por capa", "Maximum par couche", "الحد لكل طبقة")
    add(
        "超过这个数量就跳过该图层，避免一次写出过多文件。",
        "Above this number the layer is skipped, so one run does not write too many files.",
        "Por encima de este número se omite la capa, para no escribir demasiados archivos de una vez.",
        "Au-dessus de ce nombre, la couche est ignorée, pour ne pas écrire trop de fichiers d’un coup.",
        "إذا تجاوز العدد هذا الحد تُتخطى الطبقة، حتى لا تُكتب ملفات كثيرة دفعة واحدة.",
    )
    add("没有可共用的字段", "No field shared by the layers", "No hay un campo común a las capas", "Aucun champ commun aux couches", "لا يوجد حقل مشترك بين الطبقات")
    add("这个字段没有值", "This field has no values", "Este campo no tiene valores", "Ce champ n’a pas de valeurs", "هذا الحقل بلا قيم")
    add(
        "请先选择导出文件夹。工程还没保存时，需要指定一个文件夹。",
        "Choose an export folder first. An unsaved project needs a folder you pick.",
        "Elige primero la carpeta de exportación. Si el proyecto no está guardado, hay que indicar una carpeta.",
        "Choisissez d’abord un dossier d’export. Un projet non enregistré exige un dossier indiqué par vous.",
        "اختر مجلد التصدير أولًا. إذا لم يُحفظ المشروع، يلزم تحديد مجلد.",
    )
    add("没有图例分类", "No legend classes", "Sin clases de leyenda", "Pas de classes de légende", "لا فئات في المفتاح")
    add("没有字段「%s」", "No field “%s”", "No existe el campo «%s»", "Pas de champ « %s »", "لا يوجد الحقل «%s»")
    add(
        "不同值超过上限 %d。请提高「每层最多」或换一个字段。",
        "Distinct values exceed the limit of %d. Raise “Max per layer” or pick another field.",
        "Los valores distintos superan el tope de %d. Sube «Máximo por capa» o elige otro campo.",
        "Les valeurs distinctes dépassent le plafond de %d. Augmentez « Maximum par couche » ou choisissez un autre champ.",
        "القيم المختلفة تتجاوز الحد %d. ارفع «الحد لكل طبقة» أو اختر حقلًا آخر.",
    )
    add("没有可以导出的分类。%s", "Nothing to export. %s", "No hay clases que exportar. %s", "Aucune classe à exporter. %s", "لا فئات للتصدير. %s")
    add(
        "已导出 %d 个文件到：\n%s",
        "Exported %d files to:\n%s",
        "Se exportaron %d archivos a:\n%s",
        "Exporté %d fichiers vers :\n%s",
        "تم تصدير %d ملفًا إلى:\n%s",
    )
    add(
        "分类有 %d 个，超过上限 %d",
        "%d classes, over the limit of %d",
        "Hay %d clases, por encima del tope de %d",
        "%d classes, au-dessus du plafond de %d",
        "الفئات %d، وتتجاوز الحد %d",
    )
    add(
        "写成 %d 个文件，%d 个没能导出：%s",
        "Wrote %d files; %d could not be exported: %s",
        "Se escribieron %d archivos; %d no se pudieron exportar: %s",
        "%d fichiers écrits ; %d n’ont pas pu être exportés : %s",
        "كُتب %d ملفًا، وتعذر تصدير %d: %s",
    )
    add(
        "管理图层右键菜单。勾选为显示，拖动或用上下箭头改顺序。自定义名称留空就用原来的名字；写了名字后，列表显示成原名(自定义名)，图层右键里只显示括号里的名字。工具条上改过的按钮名字会同步到这里。恢复默认只还原这一页，不动工具条。下面的下拉框用来加入本插件功能。打开这一页时会读取当前右键菜单；若列表还空，先在图层面板上对图层右键一次。",
        "Manage the layer right-click menu. A check means visible. Drag, or use the arrows, to change the order. Leave the custom name blank to keep the original. After you type a name, the list shows Original(custom), and the layer right-click shows only the name in parentheses. A name changed on the toolbar is kept in step here. Reset restores only this page, not the toolbar. The list below adds this plugin’s tools. Opening this page reads the current menu. If the list is still empty, right-click a layer in the Layers panel once.",
        "Gestiona el menú contextual de las capas. La casilla significa visible. Arrastra, o usa las flechas, para cambiar el orden. Deja el nombre en blanco para conservar el original. Si escribes un nombre, la lista muestra Original(personalizado) y el clic derecho de la capa muestra solo el nombre entre paréntesis. Un nombre cambiado en la barra se refleja aquí. Restaurar solo devuelve esta página, no la barra. La lista de abajo añade herramientas de este complemento. Al abrir esta página se lee el menú actual. Si la lista sigue vacía, haz clic derecho una vez sobre una capa en el panel Capas.",
        "Gère le menu contextuel des couches. Une coche signifie visible. Glissez, ou utilisez les flèches, pour changer l’ordre. Laissez le nom vide pour garder l’original. Après un nom saisi, la liste affiche Original(personnalisé) et le clic droit de la couche n’affiche que le nom entre parenthèses. Un nom modifié dans la barre est repris ici. Réinitialiser ne restaure que cette page, pas la barre. La liste ci-dessous ajoute les outils de cette extension. Ouvrir cette page lit le menu actuel. Si la liste est encore vide, faites un clic droit une fois sur une couche dans le panneau Couches.",
        "يدير قائمة النقر بالزر الأيمن على الطبقة. التحديد يعني ظاهرًا. اسحب، أو استخدم الأسهم، لتغيير الترتيب. اترك الاسم فارغًا للإبقاء على الاسم الأصلي. بعد كتابة اسم تظهر القائمة بالشكل الاسم الأصلي(الاسم المخصص)، ونقر الطبقة بالزر الأيمن يعرض الاسم داخل القوسين فقط. الاسم الذي يُغيَّر في شريط الأدوات يتبع هنا. الاستعادة تعيد هذه الصفحة فقط، لا الشريط. القائمة أدناه تضيف أدوات هذه الإضافة. فتح هذه الصفحة يقرأ القائمة الحالية. إذا بقيت القائمة فارغة، انقر بالزر الأيمن مرة على طبقة في لوحة الطبقات.",
    )
    add("并成同一个表", "One table", "Una sola tabla", "Une seule table", "جدول واحد")
    add(
        "不勾选时，每个图层一个工作表，表名是图层名。CSV 本身不能有多个工作表，所以会写成同名的 Excel 文件。勾选后并进同一个 CSV 表：同名字段只出现一次，每个图层的字段都会保留，并加一列记下原来的图层名。",
        "When this is off, each layer is one sheet, named after the layer. CSV itself cannot hold several sheets, so a same-named Excel file is written. When it is on, everything goes into one CSV table: a shared field name appears once, every layer’s fields are kept, and a column records the source layer name.",
        "Sin marcar, cada capa es una hoja con el nombre de la capa. CSV no puede tener varias hojas, así que se escribe un Excel con el mismo nombre. Marcado, todo va a una tabla CSV: un campo con el mismo nombre aparece una vez, se conservan los campos de cada capa y una columna guarda el nombre de la capa de origen.",
        "Décochée, chaque couche est une feuille portant le nom de la couche. Un CSV ne peut pas avoir plusieurs feuilles, donc un fichier Excel du même nom est écrit. Cochée, tout va dans une table CSV : un nom de champ commun n’apparaît qu’une fois, les champs de chaque couche sont gardés, et une colonne retient le nom de la couche d’origine.",
        "بدون تحديد، كل طبقة ورقة باسم الطبقة. CSV لا يحتمل عدة أوراق، فيُكتب ملف Excel بالاسم نفسه. عند التحديد يذهب كل شيء إلى جدول CSV واحد: اسم الحقل المشترك يظهر مرة واحدة، وتُحفظ حقول كل طبقة، ويُضاف عمود باسم الطبقة الأصلية.",
    )
    add(
        "已写入 %s，共 %d 个图层。",
        "Wrote %s, %d layers.",
        "Se escribió %s, %d capas.",
        "Écrit %s, %d couches.",
        "كُتب %s، بعدد %d طبقة.",
    )
    add(
        "已写入 %s。CSV 不能分成多个工作表，已改写成 Excel：每个图层一个表，表名是图层名。",
        "Wrote %s. CSV cannot be split into sheets, so this was written as Excel: one sheet per layer, named after the layer.",
        "Se escribió %s. CSV no se puede partir en hojas, así que se escribió como Excel: una hoja por capa, con el nombre de la capa.",
        "Écrit %s. Un CSV ne peut pas être découpé en feuilles, donc ceci a été écrit en Excel : une feuille par couche, nommée comme la couche.",
        "كُتب %s. CSV لا يُقسَّم إلى أوراق، فكُتب كملف Excel: ورقة لكل طبقة باسم الطبقة.",
    )
    add(
        "只恢复图层右键菜单，不动工具条。",
        "Restore only the layer right-click menu, not the toolbar.",
        "Restaura solo el menú contextual de las capas, no la barra.",
        "Ne restaure que le menu contextuel des couches, pas la barre.",
        "يعيد قائمة النقر بالزر الأيمن على الطبقة فقط، لا شريط الأدوات.",
    )
    add("自定义名称", "Custom name", "Nombre personalizado", "Nom personnalisé", "اسم مخصص")
    add("留空使用原名", "Leave blank to keep the original name", "Déjalo vacío para usar el nombre original", "Laisser vide pour garder le nom d’origine", "اتركه فارغًا للاسم الأصلي")
    add("添加功能", "Add a tool", "Añadir una herramienta", "Ajouter un outil", "إضافة أداة")
    add("添加", "Add", "Añadir", "Ajouter", "إضافة")
    add("移除", "Remove", "Quitar", "Retirer", "إزالة")
    add("合并为一个文件", "Merge into one file", "Unir en un archivo", "Fusionner en un fichier", "دمج في ملف واحد")
    add("合并图层", "Merged layers", "Capas unidas", "Couches fusionnées", "طبقات مدمجة")
    add(
        "这一版 QGIS 不能把多个图层写进同一个文件。",
        "This QGIS version cannot write several layers into one file.",
        "Esta versión de QGIS no puede escribir varias capas en un solo archivo.",
        "Cette version de QGIS ne peut pas écrire plusieurs couches dans un seul fichier.",
        "هذا الإصدار من QGIS لا يستطيع كتابة عدة طبقات في ملف واحد.",
    )
    add(
        "勾选后，多个图层写入同一个文件。",
        "When checked, several layers are written into the same file.",
        "Si está marcado, varias capas se escriben en el mismo archivo.",
        "Si coché, plusieurs couches sont écrites dans le même fichier.",
        "عند التحديد تُكتب عدة طبقات في الملف نفسه.",
    )
    add(
        "这个格式一个文件只能放一个图层。",
        "This format can hold only one layer per file.",
        "Este formato solo admite una capa por archivo.",
        "Ce format ne peut contenir qu’une couche par fichier.",
        "هذا التنسيق يضع طبقة واحدة فقط في كل ملف.",
    )
    add(
        "已写入 %s。DXF 会丢掉大部分属性，只保留几何和图层名。",
        "Wrote %s. DXF drops most attributes and keeps only the geometry and the layer name.",
        "Se escribió %s. DXF pierde la mayoría de los atributos y solo conserva la geometría y el nombre de capa.",
        "Écrit dans %s. Le DXF perd la plupart des attributs et ne garde que la géométrie et le nom de couche.",
        "كُتب %s. يسقط DXF معظم السمات ويبقي الهندسة واسم الطبقة فقط.",
    )
    add(
        "合并文件 %s 里写入了 %d 个图层，%d 个没能写入：%s",
        "Merged file %s received %d layers; %d could not be written: %s",
        "El archivo unido %s recibió %d capas; %d no se pudieron escribir: %s",
        "Le fichier fusionné %s a reçu %d couches ; %d n’ont pas pu être écrites : %s",
        "الملف المدمج %s استقبل %d طبقة، وتعذرت كتابة %d: %s",
    )
    add("清空数据", "Clear data", "Vaciar datos", "Vider les données", "مسح البيانات")
    add("打开编辑", "Start editing", "Abrir edición", "Ouvrir l’édition", "فتح التحرير")
    add("保存关闭", "Save and close", "Guardar y cerrar", "Enregistrer et fermer", "حفظ وإغلاق")
    add("复制到空", "Copy empty", "Copiar vacío", "Copier à vide", "نسخ فارغ")
    add("复制图层", "Copy layer", "Copiar capa", "Copier la couche", "نسخ الطبقة")
    add("图层操作", "Layer actions", "Acciones de capa", "Actions de couche", "عمليات الطبقة")
    add(
        "清空数据、开关编辑，或把当前图层复制成新文件",
        "Clear data, toggle editing, or copy the current layer to a new file",
        "Vacía datos, abre o cierra la edición, o copia la capa actual a un archivo nuevo",
        "Vider les données, ouvrir ou fermer l’édition, ou copier la couche actuelle vers un nouveau fichier",
        "مسح البيانات، أو فتح التحرير وإغلاقه، أو نسخ الطبقة الحالية إلى ملف جديد",
    )
    add(
        "当前没有可处理的矢量图层。",
        "There is no vector layer to work on.",
        "No hay ninguna capa vectorial que tratar.",
        "Aucune couche vectorielle à traiter.",
        "لا توجد طبقة متجهة للمعالجة.",
    )
    add("所有图层数据已清空", "All layer data has been cleared", "Se vaciaron los datos de todas las capas", "Les données de toutes les couches ont été vidées", "مُسحت بيانات كل الطبقات")
    add("所有图层编辑模式已打开", "Editing is on for every layer", "La edición está abierta en todas las capas", "L’édition est ouverte pour toutes les couches", "فُتح التحرير لكل الطبقات")
    add(
        "所有图层已保存并退出编辑模式",
        "Every layer was saved and left editing",
        "Todas las capas se guardaron y salieron de la edición",
        "Toutes les couches ont été enregistrées et ont quitté l’édition",
        "حُفظت كل الطبقات وخرجت من التحرير",
    )
    add("确认清空", "Confirm clear", "Confirmar vaciado", "Confirmer le vidage", "تأكيد المسح")
    add(
        "将删除当前工程里全部矢量图层的全部要素。图层还在，要素删掉后不能恢复。\n请输入 OK 确认：",
        "This deletes every feature in every vector layer of the current project. The layers stay, and deleted features cannot be recovered.\nType OK to confirm:",
        "Se borrarán todas las entidades de todas las capas vectoriales del proyecto actual. Las capas siguen, y lo borrado no se puede recuperar.\nEscribe OK para confirmar:",
        "Cela supprime toutes les entités de toutes les couches vectorielles du projet en cours. Les couches restent, et les entités supprimées ne peuvent pas être récupérées.\nSaisissez OK pour confirmer :",
        "سيُحذف كل معلم في كل طبقة متجهة في المشروع الحالي. الطبقات تبقى، والمعالم المحذوفة لا تُسترجع.\nاكتب OK للتأكيد:",
    )
    add("二次确认", "Confirm again", "Segunda confirmación", "Deuxième confirmation", "تأكيد ثانٍ")
    add(
        "确认删除全部要素？这一步不能返回，也不能撤销。",
        "Delete every feature? This step cannot be undone.",
        "¿Borrar todas las entidades? Este paso no se puede deshacer.",
        "Supprimer toutes les entités ? Cette étape est irréversible.",
        "حذف كل المعالم؟ هذه الخطوة لا تُرجع ولا تُلغى.",
    )
    add(
        "连同全部要素一起复制，样式与所选图层相同。",
        "Copy every feature as well. The style matches the selected layer.",
        "Copia también todas las entidades. El estilo es el de la capa elegida.",
        "Copie aussi toutes les entités. Le style est celui de la couche choisie.",
        "انسخ كل المعالم أيضًا. النمط يطابق الطبقة المختارة.",
    )
    add(
        "不复制要素，只保留字段和样式。",
        "Do not copy features. Keep only the fields and the style.",
        "No copia entidades. Solo conserva los campos y el estilo.",
        "Ne copie pas les entités. Ne conserve que les champs et le style.",
        "لا تنسخ المعالم. أبقِ الحقول والنمط فقط.",
    )
    add(
        "这个图层没有文件路径，默认保存到工程所在文件夹。",
        "This layer has no file path. The default folder is the project folder.",
        "Esta capa no tiene ruta de archivo. La carpeta predeterminada es la del proyecto.",
        "Cette couche n’a pas de chemin de fichier. Le dossier par défaut est celui du projet.",
        "هذه الطبقة بلا مسار ملف. المجلد الافتراضي هو مجلد المشروع.",
    )
    add("_空", "_empty", "_vacio", "_vide", "_empty")
    add("保存复制图层", "Save copied layer", "Guardar la capa copiada", "Enregistrer la couche copiée", "حفظ الطبقة المنسوخة")
    add("删除全部", "Delete all", "Borrar todo", "Tout supprimer", "حذف الكل")
    add(
        "请先在图层面板选中一个矢量图层。",
        "Select a vector layer in the Layers panel first.",
        "Selecciona primero una capa vectorial en el panel Capas.",
        "Sélectionnez d’abord une couche vectorielle dans le panneau Couches.",
        "حدد أولًا طبقة متجهة في لوحة الطبقات.",
    )
    add("复制当前图层", "Copy the current layer", "Copiar la capa actual", "Copier la couche actuelle", "نسخ الطبقة الحالية")
    add("复制当前图层为空", "Copy the current layer empty", "Copiar la capa actual vacía", "Copier la couche actuelle à vide", "نسخ الطبقة الحالية فارغة")
    add(
        "当前所选图层：%s\n路径：%s\n原格式：%s\n%s\n\n下一步选择保存位置。默认就在这个文件夹，格式默认与原图层相同。",
        "Selected layer: %s\nPath: %s\nOriginal format: %s\n%s\n\nNext, choose where to save. The default is this folder, and the format defaults to the original layer.",
        "Capa seleccionada: %s\nRuta: %s\nFormato original: %s\n%s\n\nA continuación elige dónde guardar. Por defecto es esta carpeta, y el formato es el de la capa original.",
        "Couche sélectionnée : %s\nChemin : %s\nFormat d’origine : %s\n%s\n\nEnsuite, choisissez où enregistrer. Par défaut c’est ce dossier, et le format est celui de la couche d’origine.",
        "الطبقة المحددة: %s\nالمسار: %s\nالتنسيق الأصلي: %s\n%s\n\nبعدها اختر مكان الحفظ. الافتراضي هذا المجلد، والتنسيق يطابق الطبقة الأصلية.",
    )
    add("继续", "Continue", "Continuar", "Continuer", "متابعة")
    add(
        "已复制图层「%s」到：\n%s",
        "Copied layer “%s” to:\n%s",
        "Capa «%s» copiada a:\n%s",
        "Couche « %s » copiée vers :\n%s",
        "نُسخت الطبقة «%s» إلى:\n%s",
    )
    add(
        "以下图层清空失败：\n%s",
        "These layers could not be cleared:\n%s",
        "No se pudieron vaciar estas capas:\n%s",
        "Ces couches n’ont pas pu être vidées :\n%s",
        "تعذر مسح هذه الطبقات:\n%s",
    )
    add(
        "以下图层未能打开编辑：\n%s",
        "Editing could not be started on these layers:\n%s",
        "No se pudo abrir la edición en estas capas:\n%s",
        "L’édition n’a pas pu être ouverte sur ces couches :\n%s",
        "تعذر فتح التحرير لهذه الطبقات:\n%s",
    )
    add(
        "以下图层保存失败：\n%s",
        "These layers could not be saved:\n%s",
        "No se pudieron guardar estas capas:\n%s",
        "Ces couches n’ont pas pu être enregistrées :\n%s",
        "تعذر حفظ هذه الطبقات:\n%s",
    )
    add("没有写成文件。", "The file was not written.", "No se escribió el archivo.", "Le fichier n’a pas été écrit.", "لم يُكتب الملف.")
    add("文件已保存：%s", "File saved: %s", "Archivo guardado: %s", "Fichier enregistré : %s", "حُفظ الملف: %s")
    add("线标注", "Line marks", "Marcas de línea", "Repères de ligne", "علامات الخط")
    add(
        "在所选线的两端标出起点和终点，并显示长度。不改图层数据。",
        "Mark the start and end of the selected lines and show the length. Layer data is not changed.",
        "Marca el inicio y el final de las líneas seleccionadas y muestra la longitud. No cambia los datos de la capa.",
        "Marque le début et la fin des lignes sélectionnées et affichez la longueur. Les données de la couche ne changent pas.",
        "ضع علامة على بداية ونهاية الخطوط المحددة واعرض الطول. بيانات الطبقة لا تتغير.",
    )
    add("%.2f米", "%.2f m", "%.2f m", "%.2f m", "%.2f م")
    add(
        "列出所选线及长度。勾选会改 QGIS 选中；名单只在地图/表里重新选线后更新。",
        "List the selected lines and their lengths. Checking a row changes the QGIS selection. The list updates only after you select lines again on the map or in the table.",
        "Lista las líneas seleccionadas y su longitud. Marcar una fila cambia la selección de QGIS. La lista solo se actualiza cuando vuelves a seleccionar líneas en el mapa o en la tabla.",
        "Liste les lignes sélectionnées et leur longueur. Cocher une ligne change la sélection QGIS. La liste ne se met à jour qu’après une nouvelle sélection sur la carte ou dans la table.",
        "يسرد الخطوط المحددة وأطوالها. تحديد صف يغيّر تحديد QGIS. القائمة لا تتحدث إلا بعد إعادة تحديد الخطوط على الخريطة أو في الجدول.",
    )
    add("全部", "All", "Todas", "Tout", "الكل")
    add("起点%s", "Start %s", "Inicio %s", "Début %s", "البداية %s")
    add("终点%s", "End %s", "Fin %s", "Fin %s", "النهاية %s")
    add("起点%d  %s", "Start %d  %s", "Inicio %d  %s", "Début %d  %s", "البداية %d  %s")
    add(
        "只标前 %d 条，其余未显示",
        "Only the first %d are marked; the rest are not shown",
        "Solo se marcan las %d primeras; el resto no se muestra",
        "Seules les %d premières sont marquées ; le reste n’est pas affiché",
        "تُعلَّم أول %d فقط، والباقي غير معروض",
    )
    add("工具条", "Toolbar", "Barra", "Barre", "شريط الأدوات")
    add("系统属性", "Right-click", "Clic derecho", "Clic droit", "النقرة اليمنى")
    add("文件", "File", "Archivo", "Fichier", "ملف")
    add("保存合并文件", "Save merged file", "Guardar el archivo unido", "Enregistrer le fichier fusionné", "حفظ الملف المدمج")
    add("请先选择要保存的文件。", "Choose the file to save first.", "Elige primero el archivo que quieres guardar.", "Choisissez d’abord le fichier à enregistrer.", "اختر أولًا الملف الذي تريد حفظه.")
    add("这个文件已经存在，是否覆盖？", "This file already exists. Overwrite it?", "Este archivo ya existe. ¿Sobrescribirlo?", "Ce fichier existe déjà. Le remplacer ?", "هذا الملف موجود مسبقًا. هل تريد استبداله؟")
    add(
        "勾选后，多个图层写入你选定的那一个文件。",
        "When checked, the layers are written into the one file you choose.",
        "Si está marcado, las capas se escriben en el archivo que elijas.",
        "Si coché, les couches sont écrites dans le fichier que vous choisissez.",
        "عند التحديد تُكتب الطبقات في الملف الذي تختاره.",
    )
    add(
        "勾选后，这些图层的要素写入同一个文件，并加一列记下原来的图层名。点、线、面可以放在一起。",
        "When checked, features from these layers go into the same file, with a column naming the source layer. Points, lines, and polygons can share that file.",
        "Si está marcado, las entidades de estas capas van al mismo archivo, con una columna que indica la capa de origen. Puntos, líneas y polígonos pueden ir juntos.",
        "Si coché, les entités de ces couches vont dans le même fichier, avec une colonne qui nomme la couche d’origine. Points, lignes et polygones peuvent y cohabiter.",
        "عند التحديد تذهب معالم هذه الطبقات إلى الملف نفسه، مع عمود يذكر اسم الطبقة الأصلية. يمكن أن تجتمع النقاط والخطوط والمضلعات في هذا الملف.",
    )
    add("请先选择一个图层。", "Choose a layer first.", "Elige primero una capa.", "Choisissez d’abord une couche.", "اختر طبقة أولًا.")
    add("请先选择字段。", "Choose a field first.", "Elige primero un campo.", "Choisissez d’abord un champ.", "اختر حقلًا أولًا.")
    add("这个图层没有可用字段。", "This layer has no field to use.", "Esta capa no tiene ningún campo que usar.", "Cette couche n’a aucun champ utilisable.", "هذه الطبقة بلا حقل يمكن استخدامه.")
    add("在图层面板工具条上打开配置窗，从点图层框选或画线取点，按相邻两点各生成一段直线。可对参考线去重，输出到临时层或指定线图层。", "Open a configuration window from the Layers toolbar, pick points by rectangle, polygon, or a drawn line, and write one straight segment between each adjacent pair. Duplicates can be skipped against a reference line layer. Output goes to a temporary layer or a chosen line layer.", "Abre una ventana de configuración desde la barra de Capas, elige puntos con un rectángulo, un polígono o una línea dibujada, y escribe un segmento recto entre cada par adyacente. Se pueden omitir duplicados frente a una capa de líneas de referencia. La salida va a una capa temporal o a una capa de líneas elegida.", "Ouvrez une fenêtre de configuration depuis la barre Couches, choisissez des points par rectangle, polygone ou ligne dessinée, et écrivez un segment droit entre chaque paire adjacente. Les doublons peuvent être ignorés par rapport à une couche de lignes de référence. La sortie va dans une couche temporaire ou une couche de lignes choisie.", "افتح نافذة إعداد من شريط الطبقات، واختر النقاط بمستطيل أو مضلع أو خط مرسوم، واكتب قطعة مستقيمة بين كل زوج متجاور. يمكن تجاوز التكرار مقابل طبقة خطوط مرجعية. تذهب النتيجة إلى طبقة مؤقتة أو طبقة خطوط مختارة.")
    add(
        "可用「添加第三方功能」加入其它已安装插件的动作或工具箱算法。可把本插件功能、第三方动作或工具箱算法合并成组，右键里显示成类似「导出」那样的父项带子菜单；父项只展开，不执行功能。空组可留在设置里，右键菜单不显示空组。不能把组再套进组，也不要拆改 QGIS 原有子菜单。",
        "Use “Add third-party function” to add actions from other installed plugins or toolbox algorithms. Plugin functions, third-party actions, and toolbox algorithms can be merged into groups that appear on the right-click menu like Export, with a parent and a submenu. The parent only expands; it does not run a function. Empty groups may stay in settings and are hidden on the menu. Groups cannot be nested, and QGIS’s own submenus are left unchanged.",
        "Usa «Añadir función de terceros» para añadir acciones de otros complementos instalados o algoritmos de la caja de herramientas. Las funciones de este complemento, las acciones de terceros y los algoritmos se pueden unir en grupos que aparecen en el menú contextual como Exportar, con un elemento padre y un submenú. El padre solo se despliega; no ejecuta una función. Los grupos vacíos pueden quedarse en la configuración y no se muestran en el menú. No se pueden anidar grupos, y los submenús propios de QGIS no se tocan.",
        "Utilisez « Ajouter une fonction tierce » pour ajouter des actions d’autres extensions installées ou des algorithmes de la boîte à outils. Les fonctions de cette extension, les actions tierces et les algorithmes peuvent être regroupés ; le menu contextuel les affiche comme Exporter, avec un parent et un sous-menu. Le parent ne fait qu’ouvrir le sous-menu ; il n’exécute rien. Les groupes vides peuvent rester dans les paramètres et n’apparaissent pas dans le menu. Pas de groupes imbriqués, et les sous-menus propres à QGIS restent inchangés.",
        "استخدم «إضافة وظيفة طرف ثالث» لإضافة إجراءات من إضافات أخرى مثبتة أو خوارزميات صندوق الأدوات. يمكن جمع وظائف هذه الإضافة وإجراءات الأطراف الثالثة وخوارزميات الصندوق في مجموعات تظهر في قائمة النقر الأيمن مثل «تصدير»، بأصل وقائمة فرعية. الأصل يفتح القائمة الفرعية فقط ولا ينفّذ وظيفة. يمكن الإبقاء على المجموعات الفارغة في الإعدادات ولا تظهر في القائمة. لا تُتداخل المجموعات، ولا تُغيَّر القوائم الفرعية الخاصة بـ QGIS.",
    )
    add("添加第三方功能", "Add third-party function", "Añadir función de terceros", "Ajouter une fonction tierce", "إضافة وظيفة طرف ثالث")
    add("新建组", "New group", "Grupo nuevo", "Nouveau groupe", "مجموعة جديدة")
    add("重命名组", "Rename group", "Renombrar grupo", "Renommer le groupe", "إعادة تسمية المجموعة")
    add("删除组", "Delete group", "Eliminar grupo", "Supprimer le groupe", "حذف المجموعة")
    add("移入组", "Move into group", "Mover al grupo", "Déplacer dans le groupe", "نقل إلى المجموعة")
    add("移出组", "Move out of group", "Sacar del grupo", "Retirer du groupe", "إخراج من المجموعة")
    add("未命名组", "Untitled group", "Grupo sin nombre", "Groupe sans nom", "مجموعة بلا اسم")
    add("展开组", "Expand group", "Expandir grupo", "Développer le groupe", "توسيع المجموعة")
    add("折叠组", "Collapse group", "Contraer grupo", "Réduire le groupe", "طي المجموعة")
    add("组颜色配置", "Group color", "Color del grupo", "Couleur du groupe", "لون المجموعة")
    add(
        "先选中一个组，再选字体颜色。组名和组内功能用同一颜色，不铺底色。",
        "Select a group first, then choose a text color. The group title and its members share that color; no background fill.",
        "Selecciona primero un grupo y luego un color de texto. El nombre del grupo y sus elementos usan el mismo color; sin fondo.",
        "Sélectionnez d’abord un groupe, puis une couleur de texte. Le titre du groupe et ses éléments partagent cette couleur ; pas de fond.",
        "حدد مجموعة أولًا ثم اختر لون النص. اسم المجموعة وعناصرها بنفس اللون دون خلفية.",
    )
    add("最多只能建 %d 个组。", "You can create at most %d groups.", "Solo se pueden crear %d grupos como máximo.", "Vous ne pouvez créer que %d groupes au maximum.", "يمكنك إنشاء %d مجموعات كحد أقصى.")
    add(
        "勾选后，框选或画线结束即生成线段，无需再点生成。取消勾选则只取点，不写线。",
        "When checked, lines are written as soon as a selection or drawn line finishes—no separate Generate button. When unchecked, points are collected only and no lines are written.",
        "Si está marcado, las líneas se escriben en cuanto termina la selección o el trazado, sin un botón Generar aparte. Si no, solo se recogen puntos y no se escriben líneas.",
        "Si coché, les lignes sont écrites dès la fin de la sélection ou du tracé, sans bouton Générer séparé. Sinon, seuls des points sont collectés et aucune ligne n’est écrite.",
        "عند التحديد تُكتب الخطوط فور انتهاء التحديد أو الرسم دون زر توليد منفصل. عند إلغاء التحديد تُجمع النقاط فقط ولا تُكتب خطوط.",
    )
    add("已安装的其它插件和工具箱算法分开展示，可搜索。一个插件有多个动作就按项添加。不能对着当前图层使用的不能加入。不要把对方插件的子菜单整棵拆进来。", "Other installed plugins and toolbox algorithms are shown in two groups and can be searched. If a plugin has several actions, add them one by one. Items that cannot act on the current layer cannot be added. The other plugin’s submenu tree is not imported as a whole.", "Los demás complementos instalados y los algoritmos de la caja de herramientas se muestran en dos grupos y se pueden buscar. Si un complemento tiene varias acciones, se añaden una a una. Lo que no pueda actuar sobre la capa actual no se puede añadir. No se importa el árbol de submenús del otro complemento.", "Les autres extensions installées et les algorithmes de la boîte à outils sont présentés en deux groupes et sont recherchables. Si une extension a plusieurs actions, ajoutez-les une par une. Ce qui ne peut pas agir sur la couche actuelle ne peut pas être ajouté. L’arbre de sous-menus de l’autre extension n’est pas importé en bloc.", "تُعرض الإضافات الأخرى المثبتة وخوارزميات صندوق الأدوات في مجموعتين ويمكن البحث فيهما. إذا كان للإضافة عدة إجراءات تُضاف بندًا بندًا. ما لا يمكنه العمل على الطبقة الحالية لا يُضاف. لا يُستورد شجرة القوائم الفرعية للإضافة الأخرى كاملة.")
    add("只列出已安装的其它插件，可搜索。一个插件有多个动作就按项添加。不能对着当前图层使用的不能加入。不要把对方插件的子菜单整棵拆进来。", "Only other installed plugins are listed and can be searched. If a plugin has several actions, add them one by one. Items that cannot act on the current layer cannot be added. The other plugin’s submenu tree is not imported as a whole.", "Solo se listan los demás complementos instalados y se pueden buscar. Si un complemento tiene varias acciones, se añaden una a una. Lo que no pueda actuar sobre la capa actual no se puede añadir. No se importa el árbol de submenús del otro complemento.", "Seules les autres extensions installées sont listées et sont recherchables. Si une extension a plusieurs actions, ajoutez-les une par une. Ce qui ne peut pas agir sur la couche actuelle ne peut pas être ajouté. L’arbre de sous-menus de l’autre extension n’est pas importé en bloc.", "تُدرج فقط الإضافات الأخرى المثبتة ويمكن البحث فيها. إذا كان للإضافة عدة إجراءات تُضاف بندًا بندًا. ما لا يمكنه العمل على الطبقة الحالية لا يُضاف. لا يُستورد شجرة القوائم الفرعية للإضافة الأخرى كاملة.")
    add("搜索", "Search", "Buscar", "Rechercher", "بحث")
    add("已安装插件", "Installed plugins", "Complementos instalados", "Extensions installées", "الإضافات المثبتة")
    add("工具箱脚本", "Toolbox scripts", "Scripts de la caja de herramientas", "Scripts de la boîte à outils", "سكربتات صندوق الأدوات")
    add("请先选择一个组。", "Choose a group first.", "Elige primero un grupo.", "Choisissez d’abord un groupe.", "اختر مجموعة أولًا.")
    add("请先选择一项再添加。", "Choose an item first, then add it.", "Elige primero un elemento y luego añádelo.", "Choisissez d’abord un élément, puis ajoutez-le.", "اختر عنصرًا أولًا ثم أضفه.")
    add("这个功能已经在列表里了。", "This function is already in the list.", "Esta función ya está en la lista.", "Cette fonction est déjà dans la liste.", "هذه الوظيفة موجودة في القائمة مسبقًا.")
    add("对方插件已卸载，或这个功能已经不可用。", "The other plugin is uninstalled, or this function is no longer available.", "El otro complemento está desinstalado, o esta función ya no está disponible.", "L’autre extension est désinstallée, ou cette fonction n’est plus disponible.", "الإضافة الأخرى أُزيلت، أو هذه الوظيفة لم تعد متاحة.")
    add("这个功能不能对着当前图层使用。", "This function cannot be used on the current layer.", "Esta función no se puede usar sobre la capa actual.", "Cette fonction ne peut pas s’appliquer à la couche actuelle.", "لا يمكن استخدام هذه الوظيفة على الطبقة الحالية.")
    add("没有当前图层，无法运行该功能。", "There is no current layer, so this function cannot run.", "No hay una capa actual, así que esta función no se puede ejecutar.", "Il n’y a pas de couche actuelle, cette fonction ne peut donc pas s’exécuter.", "لا توجد طبقة حالية، لذلك لا يمكن تشغيل هذه الوظيفة.")
    add("请先在图层面板里选中一个图层，再添加能对着当前图层使用的功能。", "Select a layer in the Layers panel first, then add a function that can act on the current layer.", "Selecciona primero una capa en el panel de capas y luego añade una función que pueda actuar sobre la capa actual.", "Sélectionnez d’abord une couche dans le panneau Couches, puis ajoutez une fonction qui peut agir sur la couche actuelle.", "حدد طبقة أولًا في لوحة الطبقات، ثم أضف وظيفة يمكنها العمل على الطبقة الحالية.")
    add("打开该算法对话框失败。", "The algorithm dialog could not be opened.", "No se pudo abrir el cuadro del algoritmo.", "La boîte de dialogue de l’algorithme n’a pas pu s’ouvrir.", "تعذّر فتح مربع حوار الخوارزمية.")
    add("运行该功能失败。", "The function could not be run.", "No se pudo ejecutar la función.", "La fonction n’a pas pu s’exécuter.", "تعذّر تشغيل هذه الوظيفة.")
    add("多点画线", "Multi-point draw line", "Dibujar líneas entre puntos", "Tracer des lignes entre points", "رسم خطوط بين نقاط")
    add("从点图层框选或画线取点，按相邻两点各生成一段直线", "Pick points from point layers by box or a drawn line, and write one straight segment between each adjacent pair", "Elige puntos de capas de puntos con un recuadro o una línea y escribe un segmento recto entre cada par adyacente", "Choisissez des points de couches de points par cadre ou ligne dessinée, et écrivez un segment droit entre chaque paire adjacente", "اختر نقاطًا من طبقات النقاط بإطار أو خط مرسوم، واكتب قطعة مستقيمة بين كل زوج متجاور")
    add("撤销失败。", "Undo failed.", "No se pudo deshacer.", "L’annulation a échoué.", "فشل التراجع.")
    add("点图层选择（可多选）", "Point layers (multi-select)", "Capas de puntos (selección múltiple)", "Couches de points (sélection multiple)", "طبقات النقاط (اختيار متعدد)")
    add("取点方式", "Pick method", "Modo de selección", "Mode de sélection", "طريقة الاختيار")
    add("框选范围内的点（支持多图层）", "Points inside the selection (several layers allowed)", "Puntos dentro de la selección (se admiten varias capas)", "Points dans la sélection (plusieurs couches autorisées)", "النقاط داخل التحديد (يُسمح بعدة طبقات)")
    add("框选方式", "Selection method", "Método de selección", "Méthode de sélection", "أسلوب التحديد")
    add("矩形框选", "Rectangle", "Rectángulo", "Rectangle", "مستطيل")
    add("多边形框选", "Polygon", "Polígono", "Polygone", "مضلع")
    add("画线框选", "Draw line", "Dibujar línea", "Tracer une ligne", "رسم خط")
    add("吸附距离", "Snap distance", "Distancia de captura", "Distance d’accrochage", "مسافة الالتقاط")
    add("默认单位是米。地理坐标系按椭球距离计算；米制投影直接用米；非米制投影时数值为图幅单位。", "The default unit is metres. Geographic coordinates use ellipsoidal distance; metric projections use metres; non-metric projections use map units.", "La unidad predeterminada es el metro. En un sistema geográfico se usa la distancia elipsoidal; en una proyección métrica, metros; en una no métrica, las unidades del mapa.", "L’unité par défaut est le mètre. Un système géographique utilise la distance ellipsoïdale ; une projection métrique utilise le mètre ; une projection non métrique utilise les unités de la carte.", "الوحدة الافتراضية هي المتر. الإحداثيات الجغرافية تستخدم المسافة الإهليلجية؛ والإسقاط المتري يستخدم الأمتار؛ والإسقاط غير المتري يستخدم وحدات الخريطة.")
    add("参考线图层（必选）", "Reference line layer (required)", "Capa de líneas de referencia (obligatoria)", "Couche de lignes de référence (obligatoire)", "طبقة الخطوط المرجعية (إلزامية)")
    add("用于检测两点之间是否已有线，避免重复。即使允许重复，也必须选择参考线图层。", "Used to detect an existing line between two points and skip duplicates. The reference line layer is required even when duplicates are allowed.", "Sirve para detectar si ya hay una línea entre dos puntos y omitir duplicados. La capa de referencia es obligatoria aunque se permitan duplicados.", "Sert à détecter une ligne déjà présente entre deux points et à ignorer les doublons. La couche de référence reste obligatoire même si les doublons sont autorisés.", "تُستخدم لكشف وجود خط بين نقطتين وتجاوز التكرار. طبقة الخطوط المرجعية إلزامية حتى عند السماح بالتكرار.")
    add("允许生成重复的线", "Allow duplicate lines", "Permitir líneas duplicadas", "Autoriser les lignes en double", "السماح بالخطوط المكررة")
    add("输出目标", "Output", "Salida", "Sortie", "المخرج")
    add("输出方式", "Output method", "Método de salida", "Méthode de sortie", "طريقة الإخراج")
    add("临时线图层（内存）", "Temporary line layer (memory)", "Capa de líneas temporal (memoria)", "Couche de lignes temporaire (mémoire)", "طبقة خطوط مؤقتة (ذاكرة)")
    add("指定线图层", "Chosen line layer", "Capa de líneas indicada", "Couche de lignes indiquée", "طبقة خطوط محددة")
    add("临时图层坐标系", "Temporary layer CRS", "SRC de la capa temporal", "SCR de la couche temporaire", "مرجع الإحداثيات للطبقة المؤقتة")
    add("选择坐标系…", "Choose CRS…", "Elegir SRC…", "Choisir le SCR…", "اختر مرجع الإحداثيات…")
    add("自动生成设置", "Auto-generate", "Generación automática", "Génération automatique", "التوليد التلقائي")
    add("框选或画线后自动生成", "Generate automatically after selecting or drawing", "Generar automáticamente después de seleccionar o dibujar", "Générer automatiquement après la sélection ou le tracé", "ولّد تلقائيًا بعد التحديد أو الرسم")
    add("延迟（毫秒）", "Delay (ms)", "Retraso (ms)", "Délai (ms)", "التأخير (مللي ثانية)")
    add("撤销", "Undo", "Deshacer", "Annuler", "تراجع")
    add("生成线", "Generate lines", "Generar líneas", "Générer les lignes", "توليد الخطوط")
    add("刷新图层", "Refresh layers", "Actualizar capas", "Actualiser les couches", "تحديث الطبقات")
    add("请先选择至少一个点图层。", "Choose at least one point layer first.", "Elige primero al menos una capa de puntos.", "Choisissez d’abord au moins une couche de points.", "اختر طبقة نقاط واحدة على الأقل أولًا.")
    add("请先选择参考线图层。参考线图层即使允许重复也必须选择。", "Choose a reference line layer first. It is required even when duplicates are allowed.", "Elige primero una capa de líneas de referencia. Es obligatoria aunque se permitan duplicados.", "Choisissez d’abord une couche de lignes de référence. Elle reste obligatoire même si les doublons sont autorisés.", "اختر طبقة خطوط مرجعية أولًا. وهي إلزامية حتى عند السماح بالتكرار.")
    add("请先框选或画线。", "Select an area or draw a line first.", "Selecciona primero un recuadro o dibuja una línea.", "Faites d’abord une sélection ou tracez une ligne.", "حدد إطارًا أو ارسم خطًا أولًا.")
    add("不足 2 个点，未生成线。", "Fewer than 2 points, so no line was generated.", "Hay menos de 2 puntos, no se ha generado ninguna línea.", "Moins de 2 points : aucune ligne n’a été générée.", "أقل من نقطتين، لذلك لم يُولَّد أي خط.")
    add("没有可撤销的上次生成结果。", "There is no previous batch to undo.", "No hay un lote anterior que se pueda deshacer.", "Il n’y a pas de lot précédent à annuler.", "لا توجد دفعة سابقة يمكن التراجع عنها.")
    add("撤销只针对当前工程、当前输出层的上一批，不能按旧的要素编号删除。", "Undo applies only to the previous batch of the current project and current output layer. Old feature ids from another project or layer are not deleted.", "Deshacer solo afecta al lote anterior del proyecto y de la capa de salida actuales. No se borran identificadores antiguos de otro proyecto o capa.", "L’annulation ne concerne que le lot précédent du projet et de la couche de sortie actuels. Les anciens identifiants d’un autre projet ou d’une autre couche ne sont pas supprimés.", "التراجع يخص فقط الدفعة السابقة للمشروع الحالي وطبقة الإخراج الحالية. لا تُحذف أرقام المعالم القديمة من مشروع أو طبقة أخرى.")
    add("米", "m", "m", "m", "م")
    add("已画线", "Line drawn", "Línea dibujada", "Ligne tracée", "تم رسم الخط")
    add("隐藏图层列表", "Hide layer list", "Ocultar la lista de capas", "Masquer la liste des couches", "إخفاء قائمة الطبقات")
    add("显示图层列表", "Show layer list", "Mostrar la lista de capas", "Afficher la liste des couches", "إظهار قائمة الطبقات")
    add("开始画线", "Start drawing a line", "Empezar a dibujar una línea", "Commencer à tracer une ligne", "ابدأ رسم خط")
    add("开始框选", "Start selecting", "Empezar a seleccionar", "Commencer la sélection", "ابدأ التحديد")
    add("（未框选）", "(nothing selected)", "(sin selección)", "(aucune sélection)", "(لم يُحدد شيء)")
    add("选择指定线图层后，撤销会用临时字段标记本批生成的线；结束后只删除我们加上的那一列，不会删掉图层里原有的字段。", "When a chosen line layer is used, undo marks this batch with a temporary field. When finished, only the column we added is removed; existing fields on the layer are left alone.", "Si usas una capa de líneas indicada, deshacer marca este lote con un campo temporal. Al terminar, solo se elimina la columna que hemos añadido; los campos que ya tenía la capa no se tocan.", "Si vous utilisez une couche de lignes indiquée, l’annulation marque ce lot avec un champ temporaire. À la fin, seule la colonne que nous avons ajoutée est supprimée ; les champs déjà présents sur la couche restent.", "عند استخدام طبقة خطوط محددة، يعلّم التراجع هذه الدفعة بحقل مؤقت. عند الانتهاء يُحذف العمود الذي أضفناه فقط، ولا تُمس الحقول الموجودة أصلًا في الطبقة.")
    add("未设置（将用工程坐标系，再没有则用 EPSG:4326）", "Not set (the project CRS will be used, or EPSG:4326 if there is none)", "Sin definir (se usará el SRC del proyecto, o EPSG:4326 si no hay ninguno)", "Non défini (le SCR du projet sera utilisé, ou EPSG:4326 s’il n’y en a pas)", "غير معيَّن (سيُستخدم مرجع إحداثيات المشروع، أو EPSG:4326 إن لم يوجد)")
    add("（请选择参考线图层）", "(choose a reference line layer)", "(elige una capa de líneas de referencia)", "(choisissez une couche de lignes de référence)", "(اختر طبقة خطوط مرجعية)")
    add("指定的线图层无效或不存在。", "The chosen line layer is invalid or missing.", "La capa de líneas indicada no es válida o no existe.", "La couche de lignes indiquée est invalide ou absente.", "طبقة الخطوط المحددة غير صالحة أو غير موجودة.")
    add("无法创建临时线图层。", "The temporary line layer could not be created.", "No se pudo crear la capa de líneas temporal.", "La couche de lignes temporaire n’a pas pu être créée.", "تعذّر إنشاء طبقة الخطوط المؤقتة.")
    add("无法在输出图层上写入临时标记字段。", "A temporary marker field could not be added to the output layer.", "No se pudo añadir un campo de marca temporal a la capa de salida.", "Un champ de marque temporaire n’a pas pu être ajouté à la couche de sortie.", "تعذّر إضافة حقل علامة مؤقت إلى طبقة الإخراج.")
    add("无法开始编辑指定的线图层。", "The chosen line layer could not be opened for editing.", "No se pudo abrir la edición de la capa de líneas indicada.", "La couche de lignes indiquée n’a pas pu être ouverte en édition.", "تعذّر فتح تحرير طبقة الخطوط المحددة.")
    add("生成线失败。", "Generating lines failed.", "La generación de líneas ha fallado.", "La génération des lignes a échoué.", "فشل توليد الخطوط.")
    add("未生成新线，已跳过 %d 条重复线段。", "No new line was generated; %d duplicate segment(s) were skipped.", "No se ha generado ninguna línea nueva; se han omitido %d segmento(s) duplicado(s).", "Aucune nouvelle ligne n’a été générée ; %d segment(s) en double ont été ignorés.", "لم يُولَّد أي خط جديد؛ تم تجاوز %d قطعة مكررة.")
    add("已生成 %d 条线，跳过 %d 条重复线段。", "Generated %d line(s) and skipped %d duplicate segment(s).", "Se han generado %d línea(s) y se han omitido %d segmento(s) duplicado(s).", "%d ligne(s) générée(s), %d segment(s) en double ignoré(s).", "وُلِّد %d خطًا وتم تجاوز %d قطعة مكررة.")
    add("已生成 %d 条线。", "Generated %d line(s).", "Se han generado %d línea(s).", "%d ligne(s) générée(s).", "وُلِّد %d خطًا.")
    add("指定的线图层是只读的，无法写入。", "The chosen line layer is read-only and cannot be written to.", "La capa de líneas indicada es de solo lectura y no se puede escribir en ella.", "La couche de lignes indiquée est en lecture seule et ne peut pas être écrite.", "طبقة الخطوط المحددة للقراءة فقط ولا يمكن الكتابة إليها.")
    add("已框选多边形范围", "Polygon selected", "Polígono seleccionado", "Polygone sélectionné", "تم تحديد المضلع")
    add("已框选矩形范围", "Rectangle selected", "Rectángulo seleccionado", "Rectangle sélectionné", "تم تحديد المستطيل")
    add("画线起终点重合，请重新画线。", "The start and end of the line coincide. Please draw the line again.", "El inicio y el final de la línea coinciden. Vuelve a dibujar la línea.", "Le début et la fin de la ligne coïncident. Veuillez retracer la ligne.", "بداية الخط ونهايته متطابقتان. أعد رسم الخط.")
    add("沿线附近未找到点。可增大吸附距离或检查点图层。", "No point was found near the line. Increase the snap distance or check the point layers.", "No se ha encontrado ningún punto cerca de la línea. Aumenta la distancia de captura o revisa las capas de puntos.", "Aucun point n’a été trouvé près de la ligne. Augmentez la distance d’accrochage ou vérifiez les couches de points.", "لم يُعثر على نقطة قرب الخط. زد مسافة الالتقاط أو راجع طبقات النقاط.")
    add("已撤销 %d 条线。", "Undid %d line(s).", "Se han deshecho %d línea(s).", "%d ligne(s) annulée(s).", "تم التراجع عن %d خطًا.")
    add("多点画线_临时", "Multi-point lines (temporary)", "Líneas entre puntos (temporal)", "Lignes entre points (temporaire)", "خطوط بين نقاط (مؤقتة)")
    add("菜单", "Menu", "Menú", "Menu", "القائمة")
    add("右键", "Right-click", "Clic derecho", "Clic droit", "نقر يمين")
    add("工具栏", "Toolbar", "Barra de herramientas", "Barre d’outils", "شريط الأدوات")
    add(
        "管理图层右键菜单。普通项只有「菜单」勾选。与主窗口工具栏共用同一动作的项（例如切换编辑模式、保存当前图层编辑、全部编辑），以及第三方功能和工具箱算法，有「菜单」和「工具栏」两个勾选：「菜单」只决定图层右键里有没有这项，不会改原动作的显示或文字；「工具栏」对共用动作只从它已在的主窗口原工具栏拿掉或加回，对第三方插件动作按勾选显示或隐藏原工具栏按钮（与 PROC 同类做法），对工具箱算法则决定要不要在本插件图层面板工具栏挂一颗代理按钮（默认不挂，勾选后进入工具条设置，默认第 2 行）。自定义名称只作用在图层右键以及第三方代理的显示名，不会改原按钮的文字。拖动或用上下箭头改顺序。自定义名称留空就用原来的名字；写了名字后，列表显示成原名(自定义名)，图层右键里只显示括号里的名字。工具条上改过的本插件按钮名字会同步到这里。恢复默认只还原这一页的右键设置，并把从主窗口原工具栏拿掉的按钮加回去；本插件工具栏上其它按钮的显隐和顺序不动，已挂上的第三方代理会撤掉。下面的下拉框用来加入本插件功能。打开这一页时会读取当前右键菜单；若列表还空，先在图层面板上对图层右键一次。",
        "Manage the layer right-click menu. Ordinary items have only a Menu checkbox. Items that share one action with a main-window toolbar (for example Toggle Editing, Save Layer Edits, and All Edits), and third-party functions or toolbox algorithms, have two checkboxes, Menu and Toolbar: Menu only controls whether the item appears in the layer context menu, and does not change the original action’s visibility or text; Toolbar, for a shared action, only removes or puts back that button on the main-window toolbar where it already lives, for a third-party plugin action it shows or hides the original toolbar button (PROC-style); for a toolbox algorithm it decides whether to hang a proxy button on this plugin’s Layers panel toolbar (off by default; once checked it enters the toolbar settings, on row 2 by default). A custom name applies only to the layer right-click label and to a third-party proxy’s display name; it does not change the original button’s text. Drag or use the up and down arrows to change the order. Leave the custom name empty to keep the original name; once filled, the list shows Original(custom) and the layer menu shows only the name in parentheses. A renamed plugin button on the toolbar stays in step here. Restore defaults on this page resets only the right-click settings and puts back any buttons taken off a main-window toolbar; the show/hide and order of this plugin’s other toolbar buttons are left alone, and any hung third-party proxies are removed. The dropdown below adds this plugin’s own functions. Opening this page reads the current right-click menu; if the list is still empty, right-click a layer in the Layers panel first.",
        "Administra el menú contextual de la capa. Los elementos normales solo tienen la casilla Menú. Los que comparten una misma acción con una barra de la ventana principal (por ejemplo Alternar edición, Guardar ediciones de la capa y Todas las ediciones), y las funciones de terceros o los algoritmos de la caja de herramientas, tienen dos casillas, Menú y Barra de herramientas: Menú solo decide si el elemento aparece en el menú contextual de la capa, y no cambia la visibilidad ni el texto de la acción original; Barra de herramientas, en una acción compartida, solo quita o devuelve ese botón en la barra de la ventana principal donde ya está, en una acción de complemento de terceros muestra u oculta el botón original (estilo PROC); en un algoritmo decide si se cuelga un botón intermedio en la barra del panel de capas de este complemento (desactivada por defecto; al marcarla entra en los ajustes de la barra, en la fila 2 por defecto). Un nombre personalizado solo se aplica a la etiqueta del menú contextual y al nombre visible del botón intermedio de un tercero; no cambia el texto del botón original. Arrastra o usa las flechas arriba y abajo para cambiar el orden. Si dejas el nombre personalizado vacío se mantiene el original; una vez escrito, la lista muestra Original(personalizado) y el menú de la capa solo muestra el nombre entre paréntesis. Un botón de este complemento renombrado en la barra se mantiene en correspondencia aquí. Restaurar valores predeterminados en esta página solo restablece los ajustes del menú contextual y vuelve a colocar los botones quitados de una barra de la ventana principal; la visibilidad y el orden de los demás botones de la barra de este complemento no se tocan, y se retiran los botones intermedios de terceros que estuvieran colgados. La lista desplegable inferior añade funciones propias de este complemento. Al abrir esta página se lee el menú contextual actual; si la lista sigue vacía, haz primero clic derecho en una capa del panel de capas.",
        "Gérez le menu contextuel de la couche. Les éléments ordinaires n’ont que la case Menu. Ceux qui partagent une même action avec une barre de la fenêtre principale (par exemple Basculer en mode édition, Enregistrer les modifications de la couche et Toutes les éditions), ainsi que les fonctions tierces ou les algorithmes de la boîte à outils, ont deux cases, Menu et Barre d’outils : Menu décide seulement si l’élément apparaît dans le menu contextuel de la couche, sans modifier la visibilité ni le texte de l’action d’origine ; Barre d’outils, pour une action partagée, retire ou remet uniquement ce bouton sur la barre de la fenêtre principale où il se trouve déjà, pour une action de greffon tiers, affiche ou masque le bouton d’origine (style PROC) ; pour un algorithme, décide s’il faut accrocher un bouton relais sur la barre du panneau Couches de cette extension (désactivé par défaut ; une fois coché, il entre dans les réglages de la barre, à la ligne 2 par défaut). Un nom personnalisé ne s’applique qu’à l’étiquette du menu contextuel et au nom affiché du bouton relais d’un tiers ; il ne change pas le texte du bouton d’origine. Faites glisser ou utilisez les flèches haut et bas pour changer l’ordre. Laissez le nom personnalisé vide pour garder le nom d’origine ; une fois renseigné, la liste affiche Original(personnalisé) et le menu de la couche n’affiche que le nom entre parenthèses. Un bouton de cette extension renommé sur la barre reste aligné ici. Restaurer les valeurs par défaut sur cette page réinitialise uniquement les réglages du menu contextuel et remet les boutons retirés d’une barre de la fenêtre principale ; l’affichage et l’ordre des autres boutons de la barre de cette extension restent inchangés, et les boutons relais tiers accrochés sont retirés. La liste déroulante ci-dessous ajoute les fonctions propres à cette extension. L’ouverture de cette page lit le menu contextuel actuel ; si la liste est encore vide, faites d’abord un clic droit sur une couche dans le panneau Couches.",
        "أدِر قائمة النقر اليميني للطبقة. العناصر العادية فيها خانة «القائمة» فقط. العناصر التي تشارك إجراءً واحدًا مع شريط في النافذة الرئيسية (مثل تبديل التحرير وحفظ تحرير الطبقة وكل عمليات التحرير)، ووظائف الإضافات الأخرى أو خوارزميات صندوق الأدوات، لها خانتان: «القائمة» و«شريط الأدوات»: «القائمة» تحدد فقط ظهور العنصر في قائمة النقر اليميني للطبقة، ولا تغيّر ظهور الإجراء الأصلي أو نصه؛ و«شريط الأدوات» للإجراء المشترك تزيل ذلك الزر أو تعيده فقط على شريط النافذة الرئيسية الذي يوجد عليه أصلًا، ولإجراء إضافة طرف ثالث تُظهر أو تُخفي الزر الأصلي (أسلوب PROC)، ولخوارزمية صندوق الأدوات تقرر ما إذا كان سيُعلَّق زر وكيل على شريط لوحة الطبقات لهذا الملحق (غير مفعّل افتراضيًا؛ وبعد تحديده يدخل إعدادات الشريط، في الصف 2 افتراضيًا). الاسم المخصص ينطبق فقط على تسمية النقر اليميني واسم عرض وكيل الطرف الثالث، ولا يغيّر نص الزر الأصلي. اسحب أو استخدم سهمي الأعلى والأسفل لتغيير الترتيب. اترك الاسم المخصص فارغًا للإبقاء على الاسم الأصلي؛ وبعد كتابته تعرض القائمة الأصل(المخصص) وتعرض قائمة الطبقة الاسم داخل الأقواس فقط. زر هذا الملحق الذي أُعيدت تسميته على الشريط يبقى متوافقًا هنا. استعادة الافتراضي في هذه الصفحة تعيد ضبط إعدادات النقر اليميني فقط وتعيد الأزرار المُزالة من شريط النافذة الرئيسية؛ لا تُمس إظهار وترتيب أزرار شريط هذا الملحق الأخرى، وتُزال وكلاء الطرف الثالث المعلّقة. تُضيف القائمة المنسدلة أدناه وظائف هذا الملحق نفسه. فتح هذه الصفحة يقرأ قائمة النقر اليميني الحالية؛ إذا بقيت القائمة فارغة فانقر يمينًا أولًا على طبقة في لوحة الطبقات.",
    )
    add(
        "只恢复图层右键菜单，并把从主窗口原工具栏拿掉的按钮加回去。本插件工具栏上其它按钮不动；已挂上的第三方代理会撤掉。",
        "Reset only the layer right-click menu, and put back any buttons taken off a main-window toolbar. Other buttons on this plugin’s toolbar are left alone; hung third-party proxies are removed.",
        "Restablece solo el menú contextual de la capa y vuelve a colocar los botones quitados de una barra de la ventana principal. Los demás botones de la barra de este complemento no se tocan; se retiran los botones intermedios de terceros que estuvieran colgados.",
        "Réinitialise uniquement le menu contextuel de la couche, et remet les boutons retirés d’une barre de la fenêtre principale. Les autres boutons de la barre de cette extension restent ; les boutons relais tiers accrochés sont retirés.",
        "يعيد ضبط قائمة النقر اليميني للطبقة فقط، ويعيد الأزرار المُزالة من شريط النافذة الرئيسية. لا تُمس أزرار شريط هذا الملحق الأخرى؛ وتُزال وكلاء الطرف الثالث المعلّقة.",
    )
    add("名称", "Name", "Nombre", "Nom", "الاسم")
    add(
        "必须显示，不能关闭。",
        "Must stay visible and cannot be turned off.",
        "Debe permanecer visible y no se puede desactivar.",
        "Doit rester visible et ne peut pas être désactivé.",
        "يجب أن يبقى ظاهرًا ولا يمكن إيقافه.",
    )
    add(
        "在当前图层上运行该第三方功能或工具箱算法，效果与图层右键中的同一项相同。",
        "Run this third-party function or toolbox algorithm on the current layer, the same as the matching layer right-click item.",
        "Ejecuta esta función de terceros o este algoritmo de la caja de herramientas sobre la capa actual, igual que el mismo elemento del menú contextual de la capa.",
        "Exécute cette fonction tierce ou cet algorithme de la boîte à outils sur la couche actuelle, comme le même élément du menu contextuel de la couche.",
        "شغّل وظيفة الطرف الثالث أو خوارزمية صندوق الأدوات هذه على الطبقة الحالية، بنفس أثر البند المقابل في قائمة النقر اليميني للطبقة.",
    )
    add(
        '自选起点和多个线图层，检查线方向是否从起点向外连贯，端点在容差内才算相接。可在结果里翻转反向线段。',
        'Pick a start point and several line layers; check that line direction runs outward from the start, joining only when endpoints meet within the tolerance. Reverse wrong segments from the results.',
        'Elige un punto de partida y varias capas de líneas; comprueba que la dirección sale desde el inicio y solo une extremos dentro de la tolerancia. En el resultado puedes invertir tramos al revés.',
        'Choisissez un point de départ et plusieurs couches de lignes ; vérifiez que le sens part du départ et ne joint les extrémités que dans la tolérance. Inversez les segments à contresens dans le résultat.',
        'اختر نقطة بداية وعدة طبقات خطوط؛ تحقق أن الاتجاه يخرج من البداية وأن الأطراف تتصل فقط ضمن التسامح. يمكن عكس المقاطع المعكوسة من النتائج.',
    )
    add(
        '按图层符号化分类给选中要素赋值；可钉住图层，从其他层复制几何后再分类。支持跳过确认与定时自动保存。',
        'Assign selected features from the layer’s symbology classes; pin a layer to copy geometry from another layer, then classify. Skip confirmations and timed auto-save are available.',
        'Asigna entidades seleccionadas según las clases de simbología; fija una capa para copiar geometría desde otra y luego clasificar. Se puede saltar la confirmación y guardar automáticamente a tiempo.',
        'Attribuez les entités sélectionnées d’après les classes de symbologie ; épinglez une couche pour copier la géométrie d’une autre, puis classer. Confirmation facultative et enregistrement automatique temporisé.',
        'عيّن المعالم المحددة حسب فئات الترميز؛ ثبّت طبقة لنسخ الهندسة من طبقة أخرى ثم صنّف. يمكن تخطي التأكيد والحفظ التلقائي المؤقت.',
    )
    add(
        '快速分类',
        'Quick classify',
        'Clasificación rápida',
        'Classification rapide',
        'تصنيف سريع',
    )
    add(
        '没有图层',
        'No layer',
        'Sin capa',
        'Pas de couche',
        'لا طبقة',
    )
    add(
        '图层没有符号化',
        'The layer has no symbology',
        'La capa no tiene simbología',
        'La couche n’a pas de symbologie',
        'الطبقة بلا ترميز',
    )
    add(
        '无法复制符号化',
        'Cannot clone symbology',
        'No se puede copiar la simbología',
        'Impossible de cloner la symbologie',
        'تعذّر نسخ الترميز',
    )
    add(
        '无法调用 QGIS 保存',
        'Cannot call QGIS save',
        'No se puede llamar al guardado de QGIS',
        'Impossible d’appeler l’enregistrement QGIS',
        'تعذّر استدعاء حفظ QGIS',
    )
    add(
        '找不到 QGIS 自带的保存编辑',
        'QGIS Save Layer Edits action not found',
        'No se encuentra Guardar ediciones de la capa de QGIS',
        'Action Enregistrer les modifications de la couche introuvable',
        'لم يُعثر على حفظ تحرير الطبقة في QGIS',
    )
    add(
        '请选择一个矢量图层',
        'Choose a vector layer',
        'Elige una capa vectorial',
        'Choisissez une couche vectorielle',
        'اختر طبقة متجهة',
    )
    add(
        '该分类没有可反推的字段值',
        'This class has no reverse-engineered field values',
        'Esta clase no tiene valores de campo deducibles',
        'Cette classe n’a pas de valeurs de champs déductibles',
        'هذه الفئة بلا قيم حقول قابلة للاستنتاج',
    )
    add(
        '请先在地图或属性表中选中要素',
        'Select features on the map or in the attribute table first',
        'Selecciona primero entidades en el mapa o en la tabla de atributos',
        'Sélectionnez d’abord des entités sur la carte ou dans la table d’attributs',
        'حدد معالم على الخريطة أو في جدول السمات أولًا',
    )
    add(
        '规则里的字段在当前图层上不存在',
        'A field in the rule is missing on the current layer',
        'Falta en la capa actual un campo de la regla',
        'Un champ de la règle manque sur la couche actuelle',
        'حقل في القاعدة غير موجود في الطبقة الحالية',
    )
    add(
        '没有分类图层',
        'No classify layer',
        'Sin capa de clasificación',
        'Pas de couche de classification',
        'لا طبقة تصنيف',
    )
    add(
        '请先选中要复制的图层要素',
        'Select the source-layer features to copy first',
        'Selecciona primero las entidades de la capa a copiar',
        'Sélectionnez d’abord les entités de la couche à copier',
        'حدد أولًا معالم الطبقة المراد نسخها',
    )
    add(
        '几何类型不同，无法复制进分类图层（点/线/面须同类）',
        'Geometry types differ; cannot copy into the classify layer (point/line/polygon must match)',
        'Tipos de geometría distintos; no se puede copiar a la capa de clasificación (punto/línea/polígono deben coincidir)',
        'Types de géométrie différents ; impossible de copier dans la couche de classification (point/ligne/polygone doivent correspondre)',
        'أنواع الهندسة مختلفة؛ لا يمكن النسخ إلى طبقة التصنيف (نقطة/خط/مضلع يجب أن تتطابق)',
    )
    add(
        '请先在来源图层选中要素',
        'Select features on the source layer first',
        'Selecciona primero entidades en la capa de origen',
        'Sélectionnez d’abord des entités sur la couche source',
        'حدد معالم في طبقة المصدر أولًا',
    )
    add(
        '规则里的字段在分类图层上不存在',
        'A field in the rule is missing on the classify layer',
        'Falta en la capa de clasificación un campo de la règle',
        'Un champ de la règle manque sur la couche de classification',
        'حقل في القاعدة غير موجود في طبقة التصنيف',
    )
    add(
        '图层无法保存',
        'The layer cannot be saved',
        'La capa no se puede guardar',
        'La couche ne peut pas être enregistrée',
        'لا يمكن حفظ الطبقة',
    )
    add(
        '无法切到要保存的图层',
        'Cannot switch to the layer to save',
        'No se puede cambiar a la capa a guardar',
        'Impossible de passer à la couche à enregistrer',
        'تعذّر التبديل إلى الطبقة المطلوب حفظها',
    )
    add(
        '当前图层没有符号化',
        'The current layer has no symbology',
        'La capa actual no tiene simbología',
        'La couche actuelle n’a pas de symbologie',
        'الطبقة الحالية بلا ترميز',
    )
    add(
        '当前是渐变符号化，无法反推成确定字段值',
        'Graduated symbology cannot reverse into fixed field values',
        'La simbología graduada no se puede deducir a valores de campo fijos',
        'Une symbologie graduée ne se déduit pas en valeurs de champs fixes',
        'الترميز المتدرج لا يُستنتج إلى قيم حقول ثابتة',
    )
    add(
        '当前符号化不是分类/规则（%s），没有可点选的分类',
        'Current symbology is not categorized/rule-based (%s); no clickable classes',
        'La simbología actual no es categorizada/por reglas (%s); no hay clases clicables',
        'La symbologie actuelle n’est pas catégorisée/par règles (%s) ; pas de classes cliquables',
        'الترميز الحالي ليس مصنّفًا/قائمًا على قواعد (%s)؛ لا فئات قابلة للنقر',
    )
    add(
        '无法开始编辑该图层',
        'Cannot start editing this layer',
        'No se puede empezar a editar esta capa',
        'Impossible de commencer l’édition de cette couche',
        'تعذّر بدء تحرير هذه الطبقة',
    )
    add(
        '无法开始编辑分类图层',
        'Cannot start editing the classify layer',
        'No se puede empezar a editar la capa de clasificación',
        'Impossible de commencer l’édition de la couche de classification',
        'تعذّر بدء تحرير طبقة التصنيف',
    )
    add(
        '没有可复制的几何',
        'No geometry to copy',
        'No hay geometría que copiar',
        'Pas de géométrie à copier',
        'لا هندسة للنسخ',
    )
    add(
        '无法复制符号化：%s',
        'Cannot clone symbology: %s',
        'No se puede copiar la simbología: %s',
        'Impossible de cloner la symbologie : %s',
        'تعذّر نسخ الترميز: %s',
    )
    add(
        '其它值 / 空类，无法反推赋值',
        'Other / empty class; cannot reverse into an assignment',
        'Otra / clase vacía; no se puede deducir una asignación',
        'Autre / classe vide ; impossible d’en déduire une assignation',
        'قيم أخرى / فئة فارغة؛ لا يمكن استنتاج تعيين',
    )
    add(
        '表达式分类无法反推字段值',
        'Expression-based classes cannot reverse into field values',
        'Las clases por expresión no deducen valores de campo',
        'Les classes par expression ne déduisent pas de valeurs de champs',
        'فئات التعبير لا تُستنتج إلى قيم حقول',
    )
    add(
        'ELSE（其余）规则，无法反推赋值',
        'ELSE (remainder) rule; cannot reverse into an assignment',
        'Regla ELSE (resto); no se puede deducir una asignación',
        'Règle ELSE (reste) ; impossible d’en déduire une assignation',
        'قاعدة ELSE (الباقي)؛ لا يمكن استنتاج تعيين',
    )
    add(
        '字段「%s」存不下值「%s」（%s）',
        'Field “%s” cannot store value “%s” (%s)',
        'El campo «%s» no puede guardar el valor «%s» (%s)',
        'Le champ « %s » ne peut pas stocker la valeur « %s » (%s)',
        'الحقل «%s» لا يستوعب القيمة «%s» (%s)',
    )
    add(
        '读取分类失败：%s',
        'Failed to read classes: %s',
        'Error al leer las clases: %s',
        'Échec de lecture des classes : %s',
        'فشل قراءة الفئات: %s',
    )
    add(
        '来源图层和分类图层的坐标系无法转换，没有复制',
        'Source and classify layer CRS cannot be transformed; nothing copied',
        'No se puede transformar el SRC entre origen y clasificación; no se ha copiado nada',
        'Impossible de transformer le SCR source / classification ; rien n’a été copié',
        'تعذّر تحويل مرجع الإحداثيات بين المصدر والتصنيف؛ لم يُنسخ شيء',
    )
    add(
        '坐标系转换失败，没有复制：%s',
        'CRS transform failed; nothing copied: %s',
        'Falló la transformación de SRC; no se ha copiado nada: %s',
        'Échec de transformation SCR ; rien n’a été copié : %s',
        'فشل تحويل مرجع الإحداثيات؛ لم يُنسخ شيء: %s',
    )
    add(
        '写入失败',
        'Write failed',
        'Error al escribir',
        'Échec d’écriture',
        'فشل الكتابة',
    )
    add(
        'ELSE（其余）',
        'ELSE (remainder)',
        'ELSE (resto)',
        'ELSE (reste)',
        'ELSE (الباقي)',
    )
    add(
        '要素 %s 的几何无法转成分类图层的几何类型',
        'Feature %s geometry cannot convert to the classify layer geometry type',
        'La geometría de la entidad %s no se puede convertir al tipo de la capa de clasificación',
        'La géométrie de l’entité %s ne peut pas être convertie au type de la couche de classification',
        'هندسة المعلم %s لا تتحول إلى نوع هندسة طبقة التصنيف',
    )
    add(
        '复制要素失败',
        'Copying features failed',
        'Error al copiar entidades',
        'Échec de la copie des entités',
        'فشل نسخ المعالم',
    )
    add(
        '要素 %s 坐标转换失败，没有复制',
        'Feature %s coordinate transform failed; not copied',
        'Falló la transformación de coordenadas de la entidad %s; no se ha copiado',
        'Échec de transformation des coordonnées de l’entité %s ; non copiée',
        'فشل تحويل إحداثيات المعلم %s؛ لم يُنسخ',
    )
    add(
        '线方向检查',
        'Line direction check',
        'Comprobar dirección de líneas',
        'Vérifier le sens des lignes',
        'فحص اتجاه الخطوط',
    )
    add(
        '自选起点和多个线图层，检查线方向是否从起点向外连贯，端点在容差内才算相接',
        'Pick a start point and several line layers; check that line direction runs outward from the start, joining only when endpoints meet within the tolerance',
        'Elige un punto de partida y varias capas de líneas; comprueba que la dirección sale desde el inicio y solo une extremos dentro de la tolerancia',
        'Choisissez un point de départ et plusieurs couches de lignes ; vérifiez que le sens part du départ et ne joint les extrémités que dans la tolérance',
        'اختر نقطة بداية وعدة طبقات خطوط؛ تحقق أن الاتجاه يخرج من البداية وأن الأطراف تتصل فقط ضمن التسامح',
    )
    add(
        '不自动保存',
        'Do not auto-save',
        'No guardar automáticamente',
        'Ne pas enregistrer automatiquement',
        'عدم الحفظ التلقائي',
    )
    add(
        '1秒后保存',
        'Save after 1 second',
        'Guardar tras 1 segundo',
        'Enregistrer après 1 seconde',
        'الحفظ بعد ثانية واحدة',
    )
    add(
        '2秒后保存',
        'Save after 2 seconds',
        'Guardar tras 2 segundos',
        'Enregistrer après 2 secondes',
        'الحفظ بعد ثانيتين',
    )
    add(
        '3秒后保存',
        'Save after 3 seconds',
        'Guardar tras 3 segundos',
        'Enregistrer après 3 secondes',
        'الحفظ بعد 3 ثوانٍ',
    )
    add(
        '4秒后保存',
        'Save after 4 seconds',
        'Guardar tras 4 segundos',
        'Enregistrer après 4 secondes',
        'الحفظ بعد 4 ثوانٍ',
    )
    add(
        '5秒后保存',
        'Save after 5 seconds',
        'Guardar tras 5 segundos',
        'Enregistrer après 5 secondes',
        'الحفظ بعد 5 ثوانٍ',
    )
    add(
        '10秒后保存',
        'Save after 10 seconds',
        'Guardar tras 10 segundos',
        'Enregistrer après 10 secondes',
        'الحفظ بعد 10 ثوانٍ',
    )
    add(
        '按图层符号化分类给选中要素赋值；可钉住图层，从其他层复制几何后再分类',
        'Assign selected features from the layer’s symbology classes; pin a layer to copy geometry from another layer, then classify',
        'Asigna entidades seleccionadas según las clases de simbología; fija una capa para copiar geometría desde otra y luego clasificar',
        'Attribuez les entités sélectionnées d’après les classes de symbologie ; épinglez une couche pour copier la géométrie d’une autre, puis classer',
        'عيّن المعالم المحددة حسب فئات الترميز؛ ثبّت طبقة لنسخ الهندسة من طبقة أخرى ثم صنّف',
    )
    add(
        '请选择矢量图层',
        'Choose a vector layer',
        'Elige una capa vectorial',
        'Choisissez une couche vectorielle',
        'اختر طبقة متجهة',
    )
    add(
        '钉住图层',
        'Pin layer',
        'Fijar capa',
        'Épingler la couche',
        'تثبيت الطبقة',
    )
    add(
        '钉住当前分类图层。在本层选中要素再点分类：只改属性、不复制。在其他层选中再点分类：把几何复制进钉住层，再按该类规则赋值。来源图层不改；钉住层不增加来源字段。',
        'Pin the current classify layer. Select features on this layer and click a class: attributes only, no copy. Select on another layer and click a class: copy geometries into the pinned layer, then assign by that class. The source layer is unchanged; the pinned layer does not gain source fields.',
        'Fija la capa de clasificación actual. Si seleccionas en esta capa y pulsas una clase: solo atributos, sin copiar. Si seleccionas en otra capa y pulsas una clase: se copian las geometrías a la capa fijada y se asignan por esa clase. La capa de origen no cambia; la fijada no gana campos del origen.',
        'Épinglez la couche de classification actuelle. Sélection sur cette couche puis clic sur une classe : attributs seulement, pas de copie. Sélection sur une autre couche puis clic : géométries copiées dans la couche épinglée, puis assignation selon la classe. La couche source ne change pas ; la couche épinglée n’ajoute pas les champs source.',
        'ثبّت طبقة التصنيف الحالية. التحديد في هذه الطبقة ثم النقر على فئة: سمات فقط بلا نسخ. التحديد في طبقة أخرى ثم النقر: تُنسخ الهندسات إلى الطبقة المثبتة ثم تُعيَّن حسب الفئة. طبقة المصدر لا تتغير؛ والطبقة المثبتة لا تكتسب حقول المصدر.',
    )
    add(
        '默认「不自动保存」：还能撤销/回滚，QGIS 图例数量不会马上变。选「N秒后保存」：先只写入，等 N 秒再点一次 QGIS 自带的「保存图层编辑」。连续命名会按当前秒数重新计时，只存一次。中途改成不自动保存则取消这次预约。图例由 QGIS 自己刷。会保存该层当前所有未保存修改，这次不能再撤销。关掉窗口会立刻补存。3 秒已验证能跟上图例；1 秒可能仍偏赶。',
        'Default “Do not auto-save”: undo/rollback still work, and QGIS legend counts do not update at once. Choose “Save after N seconds”: writes first, then after N seconds triggers QGIS “Save Layer Edits” once. Continuous classify resets the timer to the current delay and saves once. Switching to no auto-save cancels the pending save. The legend refreshes itself. Saving commits every unsaved edit on that layer and cannot be undone. Closing the window flushes any pending save. 3 seconds keeps up with the legend; 1 second may still race.',
        'Por defecto «No guardar automáticamente»: aún se puede deshacer y los conteos de leyenda de QGIS no cambian al momento. Con «Guardar tras N segundos» se escribe primero y, tras N segundos, se dispara una vez «Guardar ediciones de la capa» de QGIS. Clasificar seguido reinicia el temporizador al retardo actual y guarda una sola vez. Pasar a no auto-guardar cancela la reserva. La leyenda la refresca QGIS. Se guardan todas las ediciones sin guardar de esa capa y ya no se puede deshacer. Al cerrar la ventana se guarda lo pendiente. 3 s sigue la leyenda; 1 s puede ir corto.',
        'Par défaut « Ne pas enregistrer automatiquement » : l’annulation reste possible et les compteurs de légende QGIS ne bougent pas tout de suite. Avec « Enregistrer après N secondes », écriture d’abord, puis après N secondes un seul « Enregistrer les modifications de la couche » de QGIS. Une classification continue relance le délai courant et n’enregistre qu’une fois. Passer à sans auto-enregistrement annule la réserve. La légende se rafraîchit toute seule. Cela enregistre toutes les modifications non sauvées de la couche et ne peut plus être annulé. Fermer la fenêtre force l’enregistrement en attente. 3 s suit la légende ; 1 s peut être trop court.',
        'الافتراضي «عدم الحفظ التلقائي»: ما زال التراجع ممكنًا وعدادات مفتاح QGIS لا تتغير فورًا. مع «الحفظ بعد N ثانية» تُكتب أولًا، ثم بعد N ثانية يُشغَّل مرة واحدة «حفظ تحرير الطبقة» في QGIS. التصنيف المتتابع يعيد ضبط المؤقت على التأخير الحالي ويحفظ مرة واحدة. التحويل إلى عدم الحفظ التلقائي يلغي الموعد. المفتاح يحدّثه QGIS. يُحفظ كل تعديل غير محفوظ في الطبقة ولا يمكن التراجع. إغلاق النافذة يحفظ المعلّق فورًا. 3 ثوانٍ تواكب المفتاح؛ ثانية واحدة قد تكون مستعجلة.',
    )
    add(
        '勾选后点分类不再确认，直接赋值',
        'When checked, clicking a class assigns at once with no confirmation',
        'Si está marcado, al pulsar una clase se asigna sin confirmar',
        'Si coché, un clic sur une classe assigne sans confirmation',
        'عند التحديد، النقر على فئة يعيّن مباشرة بلا تأكيد',
    )
    add(
        '默认不勾选：会弹出确认。勾选后直接写入。',
        'Off by default: a confirmation appears. When checked, writes at once.',
        'Desmarcado por defecto: pide confirmación. Marcado: escribe al instante.',
        'Décoché par défaut : une confirmation s’affiche. Coché : écriture immédiate.',
        'غير محدد افتراضيًا: يظهر تأكيد. عند التحديد تُكتب مباشرة.',
    )
    add(
        '刷新图例计数',
        'Refresh legend counts',
        'Actualizar conteos de leyenda',
        'Rafraîchir les compteurs de légende',
        'تحديث عدادات المفتاح',
    )
    add(
        '请先选择一个矢量图层。',
        'Choose a vector layer first.',
        'Elige primero una capa vectorial.',
        'Choisissez d’abord une couche vectorielle.',
        'اختر طبقة متجهة أولًا.',
    )
    add(
        '请在 QGIS 中选择一个矢量图层',
        'Select a vector layer in QGIS',
        'Selecciona una capa vectorial en QGIS',
        'Sélectionnez une couche vectorielle dans QGIS',
        'حدد طبقة متجهة في QGIS',
    )
    add(
        '钉住：%s',
        'Pinned: %s',
        'Fijada: %s',
        'Épinglée : %s',
        'مثبّتة: %s',
    )
    add(
        '这个分类无法从符号化规则反推出要写的字段值。',
        'This class cannot reverse its symbology rule into field values to write.',
        'Esta clase no puede deducir de la simbología los valores de campo a escribir.',
        'Cette classe ne peut pas déduire de la symbologie les valeurs de champs à écrire.',
        'لا يمكن لهذه الفئة استنتاج قيم الحقول من قاعدة الترميز.',
    )
    add(
        '请先在地图或属性表中选中要素。',
        'Select features on the map or in the attribute table first.',
        'Selecciona primero entidades en el mapa o en la tabla de atributos.',
        'Sélectionnez d’abord des entités sur la carte ou dans la table d’attributs.',
        'حدد معالم على الخريطة أو في جدول السمات أولًا.',
    )
    add(
        '已写入，但 QGIS 保存失败：%s',
        'Written, but QGIS save failed: %s',
        'Escrito, pero el guardado de QGIS falló: %s',
        'Écrit, mais l’enregistrement QGIS a échoué : %s',
        'كُتب، لكن حفظ QGIS فشل: %s',
    )
    add(
        '(未命名)',
        '(unnamed)',
        '(sin nombre)',
        '(sans nom)',
        '(بلا اسم)',
    )
    add(
        '已选中 %s 个要素。\n将归属到分类「%s」。\n写入：%s\n继续？',
        '%s feature(s) selected.\nAssign to class “%s”.\nWrite: %s\nContinue?',
        '%s entidad(es) seleccionada(s).\nAsignar a la clase «%s».\nEscribir: %s\n¿Continuar?',
        '%s entité(s) sélectionnée(s).\nAttribuer à la classe « %s ».\nÉcrire : %s\nContinuer ?',
        'تم تحديد %s معلمًا.\nالإسناد إلى الفئة «%s».\nالكتابة: %s\nمتابعة؟',
    )
    add(
        '将把 %s 个要素从「%s」复制到「%s」，并归属分类「%s」。\n来源图层不改。写入：%s\n继续？',
        'Copy %s feature(s) from “%s” into “%s” and assign class “%s”.\nThe source layer is unchanged. Write: %s\nContinue?',
        'Copiar %s entidad(es) de «%s» a «%s» y asignar la clase «%s».\nLa capa de origen no cambia. Escribir: %s\n¿Continuar?',
        'Copier %s entité(s) de « %s » vers « %s » et attribuer la classe « %s ».\nLa couche source ne change pas. Écrire : %s\nContinuer ?',
        'نسخ %s معلمًا من «%s» إلى «%s» وإسناد الفئة «%s».\nطبقة المصدر لا تتغير. الكتابة: %s\nمتابعة؟',
    )
    add(
        '不是真/假',
        'Not true/false',
        'No es verdadero/falso',
        'Pas vrai/faux',
        'ليست صح/خطأ',
    )
    add(
        '小数已四舍五入',
        'Decimal rounded',
        'Decimal redondeado',
        'Décimale arrondie',
        'قُرّب الكسر',
    )
    add(
        '不是有效日期/时间',
        'Not a valid date/time',
        'No es una fecha/hora válida',
        'Pas une date/heure valide',
        'ليست تاريخًا/وقتًا صالحًا',
    )
    add(
        '超过字段长度 %s',
        'Exceeds field length %s',
        'Supera la longitud del campo %s',
        'Dépasse la longueur du champ %s',
        'يتجاوز طول الحقل %s',
    )
    add(
        '不是有效数字',
        'Not a valid number',
        'No es un número válido',
        'Pas un nombre valide',
        'ليست رقمًا صالحًا',
    )
    add(
        '超出整数范围',
        'Outside integer range',
        'Fuera del rango entero',
        'Hors de la plage entière',
        'خارج نطاق الأعداد الصحيحة',
    )
    add(
        '不是数字',
        'Not a number',
        'No es un número',
        'Pas un nombre',
        'ليست رقمًا',
    )
    add(
        "系统属性（图层）",
        "System properties (layers)",
        "Propiedades del sistema (capas)",
        "Propriétés système (couches)",
        "خصائص النظام (الطبقات)",
    )
    add(
        "系统属性（组）",
        "System properties (groups)",
        "Propiedades del sistema (grupos)",
        "Propriétés système (groupes)",
        "خصائص النظام (المجموعات)",
    )
    add(
        "增加分割线",
        "Add separator",
        "Añadir separador",
        "Ajouter un séparateur",
        "إضافة فاصل",
    )
    add(
        "删除分割线",
        "Remove separator",
        "Quitar separador",
        "Supprimer le séparateur",
        "حذف الفاصل",
    )
    add(
        "只恢复组的右键菜单。",
        "Restore only the group right-click menu.",
        "Restaura solo el menú contextual del grupo.",
        "Ne restaure que le menu contextuel du groupe.",
        "يستعيد قائمة النقر بالزر الأيمن للمجموعة فقط.",
    )
    add(
        "自定义标注",
        "Custom label",
        "Etiqueta personalizada",
        "Étiquette personnalisée",
        "تسمية مخصصة",
    )
    add(
        "点开后列出当前图层的字段。第一项是不显示；选一个字段就把该字段当作标注。",
        "Opens a list of the current layer’s fields. The first item turns labels off; choosing a field uses that field as the label.",
        "Abre la lista de campos de la capa actual. La primera opción oculta las etiquetas; elegir un campo lo usa como etiqueta.",
        "Ouvre la liste des champs de la couche actuelle. La première entrée masque les étiquettes ; choisir un champ l’utilise comme étiquette.",
        "يفتح قائمة حقول الطبقة الحالية. البند الأول يخفي التسميات؛ واختيار حقل يجعله التسمية.",
    )
    add(
        "不显示",
        "Don’t show",
        "No mostrar",
        "Ne pas afficher",
        "عدم العرض",
    )
    add(
        "请先在图层面板里选中一个矢量图层。",
        "Select a vector layer in the Layers panel first.",
        "Primero selecciona una capa vectorial en el panel de capas.",
        "Sélectionnez d’abord une couche vectorielle dans le panneau des couches.",
        "حدد أولًا طبقة متجهة في لوحة الطبقات.",
    )
    add(
        "当前可见",
        "Current view",
        "Vista actual",
        "Vue actuelle",
        "العرض الحالي",
    )
    add(
        "手动选择区域",
        "Draw an area",
        "Dibujar un área",
        "Dessiner une zone",
        "رسم منطقة",
    )
    add(
        "只导出图层面板里勾选着的图层",
        "Export only layers checked in the Layers panel",
        "Exportar solo las capas marcadas en el panel de capas",
        "N’exporter que les couches cochées dans le panneau des couches",
        "تصدير الطبقات المحددة في لوحة الطبقات فقط",
    )
    add(
        "不勾选时，范围内的要素照样导出，即使该图层在图层面板里没勾选。",
        "When unchecked, features inside the extent are still exported even if that layer is unchecked in the Layers panel.",
        "Si no está marcada, las entidades del ámbito se exportan aunque esa capa no esté marcada en el panel de capas.",
        "Si elle est décochée, les entités de l’emprise sont quand même exportées, même si cette couche n’est pas cochée dans le panneau des couches.",
        "عند عدم التحديد تُصدَّر المعالم داخل النطاق حتى لو لم تكن الطبقة محددة في لوحة الطبقات.",
    )
    add(
        "请先在地图上框选导出范围。",
        "Draw the export area on the map first.",
        "Primero dibuja el área de exportación en el mapa.",
        "Dessinez d’abord la zone d’export sur la carte.",
        "ارسم أولًا نطاق التصدير على الخريطة.",
    )
    add(
        "没有可导出的要素。",
        "There are no features to export.",
        "No hay entidades para exportar.",
        "Aucune entité à exporter.",
        "لا توجد معالم للتصدير.",
    )
    add(
        "还没有方案",
        "No schemes yet",
        "Aún no hay esquemas",
        "Pas encore de schéma",
        "لا توجد مخططات بعد",
    )
    add(
        "菜单只列出已保存的方案。点哪一个才套用哪一个。不会自动套用，也不会自动新增方案。",
        "The menu lists only saved schemes. Click one to apply that one. Nothing is applied automatically, and no scheme is added automatically.",
        "El menú solo lista los esquemas guardados. Pulsa uno para aplicar ese. No se aplica nada solo, ni se añade un esquema solo.",
        "Le menu ne liste que les schémas enregistrés. Cliquez sur l’un d’eux pour l’appliquer. Rien n’est appliqué automatiquement, et aucun schéma n’est ajouté automatiquement.",
        "تعرض القائمة المخططات المحفوظة فقط. انقر واحدًا لتطبيقه. لا يُطبَّق شيء تلقائيًا، ولا يُضاف مخطط تلقائيًا.",
    )
    add(
        "重新载入",
        "Reload",
        "Recargar",
        "Recharger",
        "إعادة التحميل",
    )
    add(
        "按当前工程重新读取这一侧的右键菜单。已有的顺序和分组保留，缺的项会补上。",
        "Read this side's right-click menu again from the current project. Existing order and groups stay; missing entries are added.",
        "Vuelve a leer el menú contextual de este lado desde el proyecto actual. El orden y los grupos se conservan; se añaden las entradas que falten.",
        "Relit le menu contextuel de ce côté depuis le projet actuel. L’ordre et les groupes restent ; les entrées manquantes sont ajoutées.",
        "يعيد قراءة قائمة النقر بالزر الأيمن لهذا الجانب من المشروع الحالي. يبقى الترتيب والمجموعات، وتُضاف البنود الناقصة.",
    )
    add(
        "工程里还没有图层组，读不到组的右键菜单。",
        "This project has no layer group yet, so the group menu cannot be read.",
        "Este proyecto aún no tiene un grupo de capas, así que no se puede leer su menú.",
        "Ce projet n’a pas encore de groupe de couches, le menu du groupe ne peut pas être lu.",
        "لا توجد مجموعة طبقات في هذا المشروع بعد، لذا لا يمكن قراءة قائمتها.",
    )
    add(
        "工程里还没有图层，读不到图层右键菜单。",
        "This project has no layer yet, so the layer menu cannot be read.",
        "Este proyecto aún no tiene capas, así que no se puede leer su menú.",
        "Ce projet n’a pas encore de couche, le menu de la couche ne peut pas être lu.",
        "لا توجد طبقة في هذا المشروع بعد، لذا لا يمكن قراءة قائمتها.",
    )
    add(
        "只导出勾选的图层",
        "Checked layers only",
        "Solo capas marcadas",
        "Couches cochées seulement",
        "الطبقات المؤشرة فقط",
    )
    add(
        "共 %d 个",
        "%d in all",
        "%d en total",
        "%d au total",
        "%d إجمالًا",
    )
    add(
        "这个范围里将要导出的要素总数。",
        "How many features in this extent will be exported.",
        "Cuántos elementos de esta extensión se exportarán.",
        "Combien d’entités de cette étendue seront exportées.",
        "عدد العناصر التي ستُصدَّر ضمن هذا النطاق.",
    )
    add("、", ", ", ", ", ", ", "، ")
    add("{}：{}", "{}: {}", "{}: {}", "{}: {}", "{}: {}")
    return rows



_ROWS = _rows()
EN = {item[0]: item[1] for item in _ROWS}
ES = {item[0]: item[2] for item in _ROWS}
FR = {item[0]: item[3] for item in _ROWS}
AR = {item[0]: item[4] for item in _ROWS}
