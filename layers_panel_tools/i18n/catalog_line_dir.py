# -*- coding: utf-8 -*-
"""Translations for the ported line_dir package.

Includes tr() literals and Chinese legend/kind/role name parts used when
building temporary layer names (joined with _).
"""


def _rows():
    rows = []

    def add(zh, en, es, fr, ar):
        rows.append((zh, en, es, fr, ar))

    add(
        '还没有配置任何图层。',
        'No layers are configured yet.',
        'Todavía no hay ninguna capa configurada.',
        "Aucune couche n'est encore configurée.",
        'لم تُعد أي طبقة بعد.',
    )
    add(
        '所配置的图层和字段都能找到。',
        'Every configured layer and field was found.',
        'Se encontraron todas las capas y los campos configurados.',
        'Les couches et les champs configurés ont tous été trouvés.',
        'تم العثور على كل الطبقات والحقول المُعدّة.',
    )
    add(
        '字段',
        'Field',
        'Campo',
        'Champ',
        'حقل',
    )
    add(
        '只勾选要使用的分类。未勾选的要素不参与。分类来自图层符号化（分类/规则），括号内是要素数量。',
        'Check only the categories to use. Unchecked features are left out. Categories come from the layer symbology (categorized / rule-based); the number in parentheses is the feature count.',
        'Marque solo las categorías que quiera usar. Los elementos no marcados no participan. Las categorías salen de la simbología de la capa (por categorías o por reglas). El número entre paréntesis es la cantidad de elementos.',
        "Cochez seulement les catégories à utiliser. Les entités décochées ne participent pas. Les catégories viennent de la symbologie de la couche (catégorisée ou par règles). Le nombre entre parenthèses est le nombre d'entités.",
        'علّم الفئات المطلوب استخدامها فقط. العناصر غير المعلَّمة لا تشارك. الفئات من ترميز الطبقة (تصنيف أو قواعد). العدد بين القوسين هو عدد العناصر.',
    )
    add(
        '全选',
        'Select all',
        'Seleccionar todo',
        'Tout sélectionner',
        'تحديد الكل',
    )
    add(
        '全不选',
        'Select none',
        'No seleccionar nada',
        'Ne rien sélectionner',
        'عدم التحديد',
    )
    add(
        '增加',
        'Add',
        'Añadir',
        'Ajouter',
        'إضافة',
    )
    add(
        '删除',
        'Delete',
        'Eliminar',
        'Supprimer',
        'حذف',
    )
    add(
        '全部',
        'All',
        'Todos',
        'Tous',
        'الكل',
    )
    add(
        '无',
        'None',
        'Ninguno',
        'Aucun',
        'لا شيء',
    )
    add(
        '按分类筛选，未勾选的要素不参与',
        'Filter by category; unchecked features are left out',
        'Filtrar por categoría. Los elementos no marcados no participan.',
        'Filtrer par catégorie. Les entités décochées ne participent pas.',
        'تصفية حسب التصنيف. العناصر غير المعلَّمة لا تشارك.',
    )
    add(
        '图层配置',
        'Layer setup',
        'Configuración de capas',
        'Configuration des couches',
        'إعداد الطبقات',
    )
    add(
        '光交',
        'Cabinet',
        'Armario',
        'Armoire',
        'كابينة',
    )
    add(
        '字段(不用)',
        'Field (unused)',
        'Campo (no se usa)',
        'Champ (inutilisé)',
        'حقل (غير مستخدم)',
    )
    add(
        '接头',
        'Splice',
        'Empalme',
        'Épissure',
        'وصلة',
    )
    add(
        'CODE读写字段',
        'CODE read/write field',
        'Campo CODE de lectura y escritura',
        'Champ CODE en lecture et écriture',
        'حقل CODE للقراءة والكتابة',
    )
    add(
        '分纤盒',
        'FAT box',
        'Caja FAT',
        'Boîtier FAT',
        'علبة توزيع',
    )
    add(
        '户数读写字段',
        'Household read/write field',
        'Campo de hogares de lectura y escritura',
        'Champ foyers en lecture et écriture',
        'حقل الأسر للقراءة والكتابة',
    )
    add(
        '用户点',
        'User point',
        'Punto de usuario',
        'Point usager',
        'نقطة مستخدم',
    )
    add(
        '户数读取字段',
        'Household read field',
        'Campo de hogares de lectura',
        'Champ foyers en lecture',
        'حقل الأسر للقراءة',
    )
    add(
        '光缆',
        'Cable',
        'Cable',
        'Câble',
        'كابل',
    )
    add(
        '户数写入字段',
        'Household write field',
        'Campo de hogares de escritura',
        'Champ foyers en écriture',
        'حقل الأسر للكتابة',
    )
    add(
        '皮线',
        'Drop',
        'Acometida',
        'Branchement',
        'كبل إسقاط',
    )
    add(
        '取消',
        'Cancel',
        'Cancelar',
        'Annuler',
        'إلغاء',
    )
    add(
        '保存',
        'Save',
        'Guardar',
        'Enregistrer',
        'حفظ',
    )
    add(
        '参数配置',
        'Parameters',
        'Parámetros',
        'Paramètres',
        'المعاملات',
    )
    add(
        '吸附按米计算。图层会先转到局部米制，工程默认 4326 或其它坐标系都可以。',
        'Snapping is measured in metres. Layers are transformed to a local metric CRS first. Project CRS 4326 or any other CRS is fine.',
        'El ajuste se mide en metros. Las capas se transforman primero a un SRC métrico local. Sirve el SRC del proyecto 4326 o cualquier otro.',
        "L'accrochage est en mètres. Les couches sont d'abord transformées vers un SCR métrique local. Le SCR du projet 4326 ou un autre convient.",
        'الالتقاط بالمتر. تُحوَّل الطبقات أولًا إلى نظام متري محلي. نظام المشروع 4326 أو غيره مناسب.',
    )
    add(
        ' 米',
        ' m',
        ' m',
        ' m',
        ' م',
    )
    add(
        '吸附容差',
        'Snap tolerance',
        'Tolerancia de ajuste',
        "Tolérance d'accrochage",
        'سماحية الالتقاط',
    )
    add(
        '顺时针',
        'Clockwise',
        'Horario',
        'Sens horaire',
        'مع عقارب الساعة',
    )
    add(
        '逆时针',
        'Counter-clockwise',
        'Antihorario',
        'Sens antihoraire',
        'عكس عقارب الساعة',
    )
    add(
        '方向排序',
        'Direction sort',
        'Orden de dirección',
        'Ordre de direction',
        'ترتيب الاتجاه',
    )
    add(
        '起始角度',
        'Start angle',
        'Ángulo inicial',
        'Angle de départ',
        'زاوية البداية',
    )
    add(
        '0°正北，90°正东，180°正南，270°正西。按出线第一段，不是线末端。方向和起始角只给光交 ODF：第一段主干一样长时才用来打破平局。接头分叉比该方向全部户数和到下一接头的主干长度，不用角度。分纤盒链路比户数和到首盒的线长，也不用角度。赋值和命名方案在「方案」页，六个功能各自一份。',
        '0° es el norte, 90° el este, 180° el sur y 270° el oeste. El ángulo usa el primer segment, no el extremo lejano. La direction y el ángulo inicial solo valen para los empates ODF del cabinet. Los ramales de splice comparan households y longitud de feeder, no el ángulo. Las cadenas de FAT box comparan households y longitud hasta la primera caja, no el ángulo. Los esquemas de relleno y de nombre están en la página Scheme, uno por herramienta.',
        '0° es el norte, 90° el este, 180° el sur y 270° el oeste. El ángulo usa el primer tramo, no el extremo lejano. La dirección y el ángulo inicial solo valen para los empates ODF del armario. Los ramales de empalme comparan hogares y longitud de alimentador, no el ángulo. Las cadenas de caja FAT comparan hogares y longitud hasta la primera caja, no el ángulo. Los esquemas de relleno y de nombre están en la página Esquema, uno por herramienta.',
        "0° est le nord, 90° l'est, 180° le sud, 270° l'ouest. L'angle utilise le premier tronçon, pas l'extrémité lointaine. Le sens et l'angle de départ ne servent qu'aux égalités ODF de l'armoire. Les branches d'épissure comparent les foyers et la longueur d'alimentation, pas l'angle. Les chaînes FAT comparent les foyers et la longueur jusqu'au premier FAT, pas l'angle. Les schémas de remplissage et de nommage sont dans la page Schéma, un par outil.",
        '0° شمال، 90° شرق، 180° جنوب، 270° غرب. الزاوية تستخدم القطعة الأولى لا الطرف البعيد. الاتجاه وزاوية البداية لكابينة ODF فقط عند تعادل أول جزء تغذية. تفرعات الوصلة تقارن الأسر وطول التغذية لا الزاوية. سلاسل علبة التوزيع تقارن الأسر والطول إلى أول علبة لا الزاوية. مخططات الملء والتسمية في صفحة المخطط، واحد لكل أداة.',
    )
    add(
        '吸附与排序',
        'Snap and sort',
        'Ajuste y orden',
        'Accrochage et ordre',
        'الالتقاط والترتيب',
    )
    add(
        '方案',
        'Scheme',
        'Esquema',
        'Schéma',
        'مخطط',
    )
    add(
        '接头 CODE 前缀',
        'Splice CODE prefix',
        'Prefijo CODE del empalme',
        "Préfixe CODE de l'épissure",
        'بادئة CODE للوصلة',
    )
    add(
        '分纤盒 CODE 前缀',
        'FAT CODE prefix',
        'Prefijo CODE de la caja FAT',
        'Préfixe CODE du boîtier FAT',
        'بادئة CODE لعلبة التوزيع',
    )
    add(
        '光缆 CODE 前缀',
        'Cable CODE prefix',
        'Prefijo CODE del cable',
        'Préfixe CODE du câble',
        'بادئة CODE للكابل',
    )
    add(
        '接头前缀用于接头 CODE。分纤盒前缀用于分纤盒 CODE。光缆前缀用于主干/配线 CODE。',
        'El prefijo de splice es para el CODE del splice. El de la FAT box es para el CODE de la caja. El del cable es para el CODE de feeder y distribution.',
        'El prefijo de empalme es para el CODE del empalme. El de la caja FAT es para el CODE de la caja. El del cable es para el CODE de alimentador y distribución.',
        "Le préfixe d'épissure sert au CODE d'épissure. Celui du FAT sert au CODE du FAT. Celui du câble sert au CODE d'alimentation et de distribution.",
        'بادئة الوصلة لـ CODE الوصلة. بادئة علبة التوزيع لـ CODE العلبة. بادئة الكابل لـ CODE التغذية والتوزيع.',
    )
    add(
        '变量配置',
        'Variables',
        'Variables',
        'Variables',
        'المتغيرات',
    )
    add(
        '导出当前全部图层配置和参数（含分类筛选、字段、容差、各功能方案、前缀、城市/PM）。导入是全覆盖：立刻替换现有配置并保存，点取消也不会还原。',
        'Exporta toda la setup de capas y los parameters (filtros de category, campos, tolerance, esquemas, prefijos, ciudad/PM). Importar lo sustituye todo al momento y lo guarda. Cancel no restaura la setup anterior.',
        'Exporta toda la configuración de capas y los parámetros (filtros de categoría, campos, tolerancia, esquemas, prefijos, ciudad/PM). Importar lo sustituye todo al momento y lo guarda. Cancelar no restaura la configuración anterior.',
        "Exporte toute la configuration des couches et les paramètres (filtres de catégorie, champs, tolérance, schémas, préfixes, ville/PM). L'import remplace tout immédiatement et l'enregistre. Annuler ne restaure pas la configuration précédente.",
        'يصدّر كل إعداد الطبقات والمعاملات (تصفية الفئات، الحقول، السماحية، المخططات، البادئات، المدينة/PM). الاستيراد يستبدل الكل فورًا ويحفظه. الإلغاء لا يعيد الإعداد السابق.',
    )
    add(
        '导出…',
        'Export…',
        'Exportar…',
        'Exporter…',
        'تصدير…',
    )
    add(
        '导入…',
        'Import…',
        'Importar…',
        'Importer…',
        'استيراد…',
    )
    add(
        '导入导出',
        'Import / Export',
        'Importar / Exportar',
        'Importer / Exporter',
        'استيراد / تصدير',
    )
    add(
        '组网骨架不变：光交 → 主干 → 接头 → 配线 → 分纤盒 → 入户。这里只改每个功能怎么写编号。六个功能各自独立，互不影响。以后加方案：在 ntal_scheme.py 的 ACTION_SCHEMES 对应功能下追加一行即可。',
        'La forma de la red no cambia: cabinet → feeder → splice → distribution → FAT box → usuario. Esta página solo cambia cómo escribe el número cada herramienta. Las seis son independientes. Para añadir un scheme, agregue una fila bajo esa herramienta en ACTION_SCHEMES de ntal_scheme.py.',
        'La forma de la red no cambia: armario → alimentador → empalme → distribución → caja FAT → usuario. Esta página solo cambia cómo escribe el número cada herramienta. Las seis son independientes. Para añadir un esquema, agregue una fila bajo esa herramienta en ACTION_SCHEMES de ntal_scheme.py.',
        'La forme du réseau ne change pas : armoire → alimentation → épissure → distribution → FAT → usager. Cette page ne change que la façon dont chaque outil écrit le numéro. Les six outils sont indépendants. Pour ajouter un schéma, ajoutez une ligne sous cet outil dans ACTION_SCHEMES de ntal_scheme.py.',
        'شكل الشبكة لا يتغير: كابينة → تغذية → وصلة → توزيع → علبة توزيع → مستخدم. هذه الصفحة تغيّر فقط كيف تكتب كل أداة الرقم. الأدوات الست مستقلة. لإضافة مخطط، أضف صفًا تحت تلك الأداة في ACTION_SCHEMES داخل ntal_scheme.py.',
    )
    add(
        '图层',
        'Layer',
        'Capa',
        'Couche',
        'طبقة',
    )
    add(
        '分类',
        'Category',
        'Categoría',
        'Catégorie',
        'تصنيف',
    )
    add(
        '{}类',
        '{} classes',
        '{} clases',
        '{} classes',
        '{} فئات',
    )
    add(
        '只选光交图层。当前功能不读、不写这个字段。',
        'Choose solo la layer de points del cabinet. Esta herramienta no lee ni escribe este campo.',
        'Elija solo la capa de puntos del armario. Esta herramienta no lee ni escribe este campo.',
        "Choisissez seulement la couche de points de l'armoire. Cet outil ne lit ni n'écrit ce champ.",
        'اختر طبقة نقاط الكابينة فقط. هذه الأداة لا تقرأ هذا الحقل ولا تكتبه.',
    )
    add(
        '读写。接头命名：写入 CODE。分纤盒命名、光缆命名：读取 CODE。',
        'Lectura y escritura. El nombre del splice escribe CODE. El nombre de la FAT box y el del cable leen CODE.',
        'Lectura y escritura. El nombre del empalme escribe CODE. El nombre de la caja FAT y el del cable leen CODE.',
        "Lecture et écriture. Le nommage de l'épissure écrit CODE. Le nommage FAT et celui du câble lisent CODE.",
        'قراءة وكتابة. تسمية الوصلة تكتب CODE. تسمية علبة التوزيع وتسمية الكابل تقرآن CODE.',
    )
    add(
        '读写。分纤盒赋值：写入户数。光缆赋值、接头/分纤盒命名：读取户数。',
        'Lectura y escritura. El relleno de la FAT box escribe households. El relleno del cable y los nombres de splice y FAT box leen households.',
        'Lectura y escritura. El relleno de la caja FAT escribe hogares. El relleno del cable y los nombres de empalme y caja FAT leen hogares.',
        "Lecture et écriture. Le remplissage FAT écrit les foyers. Le remplissage du câble et les nommages d'épissure et de FAT lisent les foyers.",
        'قراءة وكتابة. ملء علبة التوزيع يكتب الأسر. ملء الكابل وتسمية الوصلة والعلبة تقرأ الأسر.',
    )
    add(
        '读写。分纤盒命名：写入 CODE。光缆命名：读取 CODE。',
        'Lectura y escritura. El nombre de la FAT box escribe CODE. El nombre del cable lee CODE.',
        'Lectura y escritura. El nombre de la caja FAT escribe CODE. El nombre del cable lee CODE.',
        'Lecture et écriture. Le nommage FAT écrit CODE. Le nommage du câble lit CODE.',
        'قراءة وكتابة. تسمية علبة التوزيع تكتب CODE. تسمية الكابل تقرأ CODE.',
    )
    add(
        '读取。皮线赋值从这里读用户户数。分纤盒赋值用它核对总户数，不按用户点累加。',
        'Lectura. El relleno de la drop lee aquí los households del usuario. El relleno de la FAT box lo usa para comprobar el total, no sumando points de usuario.',
        'Lectura. El relleno de la acometida lee aquí los hogares del usuario. El relleno de la caja FAT lo usa para comprobar el total, no sumando puntos de usuario.',
        "Lecture. Le remplissage du branchement lit ici les foyers usager. Le remplissage FAT s'en sert pour vérifier le total, sans additionner les points usager.",
        'قراءة. ملء كبل الإسقاط يقرأ أسر المستخدم من هنا. ملء علبة التوزيع يستخدمه للتحقق من المجموع، لا بجمع نقاط المستخدم.',
    )
    add(
        'CODE写入字段',
        'CODE write field',
        'Campo CODE de escritura',
        'Champ CODE en écriture',
        'حقل CODE للكتابة',
    )
    add(
        '写入。光缆赋值把分纤盒户数写到这里。主干/配线按两端点判定。',
        'Escritura. El relleno del cable escribe aquí los households de la FAT box. El feeder y la distribution se deciden por los dos extremos.',
        'Escritura. El relleno del cable escribe aquí los hogares de la caja FAT. El alimentador y la distribución se deciden por los dos extremos.',
        "Écriture. Le remplissage du câble écrit ici les foyers du boîtier FAT. L'alimentation et la distribution se jugent par les deux extrémités.",
        'كتابة. ملء الكابل يكتب أسر علبة التوزيع هنا. التغذية والتوزيع يُحدَّدان من الطرفين.',
    )
    add(
        '写入。光缆命名把生成的 CODE 写到这里。',
        'Escritura. El nombre del cable escribe aquí el CODE generado.',
        'Escritura. El nombre del cable escribe aquí el CODE generado.',
        'Écriture. Le nommage du câble écrit ici le CODE généré.',
        'كتابة. تسمية الكابل تكتب CODE المولَّد هنا.',
    )
    add(
        '主干和配线用同一图层。光交–接头、接头–接头是主干；接头–分纤盒、分纤盒–分纤盒是配线。',
        'El feeder y la distribution usan la misma layer. Cabinet–splice y splice–splice son feeder; splice–FAT box y FAT box–FAT box son distribution.',
        'El alimentador y la distribución usan la misma capa. Armario–empalme y empalme–empalme son alimentador; empalme–caja FAT y caja FAT–caja FAT son distribución.',
        "L'alimentation et la distribution partagent une couche. Armoire–épissure et épissure–épissure sont l'alimentation ; épissure–FAT et FAT–FAT sont la distribution.",
        'التغذية والتوزيع تستخدمان الطبقة نفسها. كابينة–وصلة ووصلة–وصلة تغذية؛ وصلة–علبة وعلبة–علبة توزيع.',
    )
    add(
        '读写。皮线赋值：写入户数。分纤盒赋值：读取户数。',
        'Lectura y escritura. El relleno de la drop escribe households. El relleno de la FAT box lee households.',
        'Lectura y escritura. El relleno de la acometida escribe hogares. El relleno de la caja FAT lee hogares.',
        'Lecture et écriture. Le remplissage du branchement écrit les foyers. Le remplissage FAT lit les foyers.',
        'قراءة وكتابة. ملء كبل الإسقاط يكتب الأسر. ملء علبة التوزيع يقرأ الأسر.',
    )
    add(
        '皮线赋值把用户点户数写到这里。分纤盒赋值再把这里的户数加到所出的分纤盒。',
        'El relleno de la drop escribe aquí los households del point de usuario. El relleno de la FAT box suma esos households a la caja de la que salen.',
        'El relleno de la acometida escribe aquí los hogares del punto de usuario. El relleno de la caja FAT suma esos hogares a la caja de la que salen.',
        "Le remplissage du branchement écrit ici les foyers du point usager. Le remplissage FAT ajoute ensuite ces foyers au boîtier d'où ils sortent.",
        'ملء كبل الإسقاط يكتب أسر نقطة المستخدم هنا. ملء علبة التوزيع يضيف هذه الأسر إلى العلبة التي تخرج منها.',
    )
    add(
        '筛选分类 — {}',
        'Filter categories — {}',
        'Filtrar categorías — {}',
        'Filtrer les catégories — {}',
        'تصفية الفئات — {}',
    )
    add(
        '%s。没有可筛选的分组时，将使用该图层全部要素。',
        '%s. When there is no filterable group, every feature on the layer is used.',
        '%s. Si no hay un grupo filtrable, se usan todos los elementos de la capa.',
        '%s. Sans groupe filtrable, tous les éléments de la couche sont utilisés.',
        '%s. إذا لم توجد مجموعة قابلة للتصفية، تُستخدم كل عناصر الطبقة.',
    )
    add(
        '(可选)',
        '(optional)',
        '(opcional)',
        '(facultatif)',
        '(اختياري)',
    )
    add(
        '图层不存在: %s',
        'Layer does not exist: %s',
        'La capa no existe: %s',
        'Couche introuvable : %s',
        'الطبقة غير موجودة: %s',
    )
    add(
        '空',
        'Empty',
        'Vacío',
        'Vide',
        'فارغ',
    )
    add(
        '找不到图层：{}',
        'Layer not found: {}',
        'No se encontró la capa: {}',
        'Couche introuvable : {}',
        'لم تُعثر على الطبقة: {}',
    )
    add(
        '有多个同名图层「{}」，请在图层配置里重新选一次再保存。',
        'Several layers are named “{}”. Pick the layer again in the setup and save.',
        'Hay varias capas llamadas «{}». Vuelva a elegir la capa en la configuración y guarde.',
        "Plusieurs couches s'appellent « {} ». Choisissez à nouveau la couche dans la configuration, puis enregistrez.",
        'توجد عدة طبقات باسم «{}». أعد اختيار الطبقة في الإعداد ثم احفظ.',
    )
    add(
        '图层 {} 的分类筛选有 {} 类对不上当前符号（已按分类名称兜底匹配），建议重新筛选。',
        'Layer {} has {} filter classes that no longer match the current symbols (matched by category name as a fallback). Filter again.',
        'La capa {} tiene {} categorías que ya no coinciden con los símbolos actuales (se emparejaron por nombre). Vuelva a filtrar.',
        'La couche {} a {} catégories qui ne correspondent plus aux symboles actuels (appariées par nom en repli). Filtrez à nouveau.',
        'الطبقة {} فيها {} فئات لم تعد تطابق الرموز الحالية (طُوبقت بالاسم احتياطًا). أعد التصفية.',
    )
    add(
        '找不到字段：{}（图层 {}）',
        'Field not found: {} (layer {})',
        'No se encontró el campo: {} (capa {})',
        'Champ introuvable : {} (couche {})',
        'لم يُعثر على الحقل: {} (الطبقة {})',
    )
    add(
        '未选',
        'None selected',
        'Ninguno',
        'Aucun',
        'غير محدد',
    )
    add(
        '(空)',
        '(blank)',
        '(vacío)',
        '(vide)',
        '(فارغ)',
    )
    add(
        '全面检测',
        'Full check',
        'Comprobación completa',
        'Contrôle complet',
        'فحص كامل',
    )
    add(
        '组网骨架固定（光交→主干→接头→配线→分纤盒→入户）。命名方案见参数「方案」页。',
        'La forma de la red es fija (cabinet → feeder → splice → distribution → FAT box → usuario). Los esquemas de nombre están en la página Scheme.',
        'La forma de la red es fija (armario → alimentador → empalme → distribución → caja FAT → usuario). Los esquemas de nombre están en la página Esquema.',
        'La forme du réseau est fixe (armoire → alimentation → épissure → distribution → FAT → usager). Les schémas de nommage sont dans la page Schéma.',
        'شكل الشبكة ثابت (كابينة → تغذية → وصلة → توزيع → علبة توزيع → مستخدم). مخططات التسمية في صفحة المخطط.',
    )
    add(
        '结果窗置顶、不挡地图。检查页看问题列表，可修复页只列方向反了的线。',
        'The result window stays on top and does not block the map. The Check page lists issues; the Fixable page lists only reversed lines.',
        'La ventana de resultados queda encima y no tapa el mapa. Comprobar lista los problemas. Reparable solo lista las líneas invertidas.',
        'La fenêtre de résultat reste au-dessus et ne bloque pas la carte. Contrôle liste les problèmes. Réparable ne liste que les lignes inversées.',
        'نافذة النتيجة تبقى في الأعلى ولا تحجب الخريطة. الفحص يسرد المشكلات. القابل للإصلاح يسرد الخطوط المعكوسة فقط.',
    )
    add(
        '选择要检查的网络问题',
        'Choose which network issues to check',
        'Elija qué problemas de red comprobar',
        'Choisir les problèmes de réseau à contrôler',
        'اختر مشكلات الشبكة المطلوب فحصها',
    )
    add(
        '按下面每一类单独勾选。默认全部检查。反选会把当前勾选反过来。检测完会留下结果窗：硬错误、软错误、警告写在「检查」页，方向反了的线在「可修复」页，可以翻转。地图图层在「全面检测」组里，硬错误、软错误、警告分开。',
        'Marque cada clase por separado. Por defecto se comprueba todo. Reverse cambia las marcas actuales. Al terminar queda una ventana: los hard errors, leves y warnings están en Comprobar, y las lines reversed en Fixable para poder invertirlas. Las capas del mapa van al grupo Full check, separadas igual.',
        'Marque cada clase por separado. Por defecto se comprueba todo. Invertir cambia las marcas actuales. Al terminar queda una ventana: los errores duros, leves y avisos están en Comprobar, y las líneas invertidas en Reparable para poder invertirlas. Las capas del mapa van al grupo Comprobación completa, separadas igual.',
        'Cochez chaque classe séparément. Tout est contrôlé par défaut. Inverser retourne les coches actuelles. Une fenêtre reste ensuite : erreurs dures, souples et avertissements dans Contrôle, lignes inversées dans Réparable pour les retourner. Les couches de la carte vont dans le groupe Contrôle complet, séparées de la même façon.',
        'علّم كل فئة على حدة. الافتراضي فحص الكل. العكس يقلب العلامات الحالية. بعد الفحص تبقى نافذة: الأخطاء الصارمة والمرنة والتحذيرات في صفحة الفحص، والخطوط المعكوسة في القابل للإصلاح ويمكن قلبها. طبقات الخريطة في مجموعة الفحص الكامل، مفصولة بالطريقة نفسها.',
    )
    add(
        '反选',
        'Invert selection',
        'Invertir',
        'Inverser',
        'عكس',
    )
    add(
        '开始检测',
        'Start check',
        'Iniciar comprobación',
        'Lancer le contrôle',
        'بدء الفحص',
    )
    add(
        '吸附容差必须大于 0。',
        'Snap tolerance must be greater than 0.',
        'La tolerancia de ajuste debe ser mayor que 0.',
        "La tolérance d'accrochage doit être supérieure à 0.",
        'يجب أن تكون سماحية الالتقاط أكبر من 0.',
    )
    add(
        '请先在图层配置里选择要检测的点线图层。',
        'Choose the point and line layers to check in the layer setup first.',
        'Elija primero en la configuración las capas de puntos y líneas que hay que comprobar.',
        "Choisissez d'abord dans la configuration les couches de points et de lignes à contrôler.",
        'اختر أولًا في إعداد الطبقات طبقات النقاط والخطوط المطلوب فحصها.',
    )
    add(
        '线方向从光交往外走，请先配置光交。',
        'Line direction walks outward from the cabinet. Configure the cabinet first.',
        'La dirección sale del armario hacia fuera. Configure primero el armario.',
        "Le sens part de l'armoire vers l'extérieur. Configurez d'abord l'armoire.",
        'اتجاه الخط يسير من الكابينة إلى الخارج. اضبط الكابينة أولًا.',
    )
    add(
        '线方向至少需要光缆或皮线。',
        'Line direction needs at least the cable or the drop layer.',
        'La dirección necesita al menos el cable o la acometida.',
        'Le sens exige au moins le câble ou le branchement.',
        'اتجاه الخط يحتاج الكابل أو كبل الإسقاط على الأقل.',
    )
    add(
        'NTAL 全面检测',
        'Full network check',
        'Comprobación completa de la red',
        'Contrôle complet du réseau',
        'فحص الشبكة الكامل',
    )
    add(
        '没有勾选检查项。',
        'No check items are selected.',
        'No hay ninguna comprobación marcada.',
        "Aucun contrôle n'est coché.",
        'لم يُعلَّم أي فحص.',
    )
    add(
        '勾选的类里没有发现问题。',
        'No problems found in the checked classes.',
        'Las clases marcadas no tienen problemas.',
        "Les classes cochées n'ont aucun problème.",
        'الفئات المعلَّمة بلا مشكلات.',
    )
    add(
        '硬错误 {}，软错误 {}，警告 {}。',
        'Hard errors {}, soft errors {}, warnings {}.',
        'Duros {}, leves {}, avisos {}.',
        'Dures {}, souples {}, avertissements {}.',
        'صارمة {}، مرنة {}، تحذيرات {}.',
    )
    add(
        '已生成图层：',
        'Layers created: ',
        'Capas creadas: ',
        'Couches créées : ',
        'تم إنشاء الطبقات: ',
    )
    add(
        '配置不完整',
        'Setup incomplete',
        'La configuración está incompleta',
        'La configuration est incomplète',
        'الإعداد غير مكتمل',
    )
    add(
        '硬错误',
        'Hard error',
        'Error duro',
        'Erreur dure',
        'خطأ صارم',
    )
    add(
        '软错误',
        'Soft error',
        'Error leve',
        'Erreur souple',
        'خطأ مرن',
    )
    add(
        '警告',
        'Warning',
        'Aviso',
        'Avertissement',
        'تحذير',
    )
    add(
        '没有光交。',
        'There are no cabinet.',
        'No hay armario.',
        "Pas d'armoire.",
        'لا توجد كابينة.',
    )
    add(
        '线',
        'Line',
        'Línea',
        'Ligne',
        'خط',
    )
    add(
        '点',
        'Point',
        'Punto',
        'Point',
        'نقطة',
    )
    add(
        '用户',
        'User',
        'Usuario',
        'Usager',
        'مستخدم',
    )
    add(
        '请选择光交点图层。',
        'Choose la layer de points del cabinet.',
        'Elija la capa de puntos del armario.',
        "Choisissez la couche de points de l'armoire.",
        'اختر طبقة نقاط الكابينة.',
    )
    add(
        '请选择分纤盒点图层。',
        'Choose la layer de points de la FAT box.',
        'Elija la capa de puntos de la caja FAT.',
        'Choisissez la couche de points du FAT.',
        'اختر طبقة نقاط علبة التوزيع.',
    )
    add(
        '请选择光缆图层。',
        'Choose la layer de cable.',
        'Elija la capa de cable.',
        'Choisissez la couche de câble.',
        'اختر طبقة الكابل.',
    )
    add(
        '请选择分纤盒户数字段（线赋值按此字段读取）。',
        'Choose el campo de households de la FAT box. El relleno del cable lo lee.',
        'Elija el campo de hogares de la caja FAT. El relleno del cable lo lee.',
        'Choisissez le champ foyers du FAT. Le remplissage du câble le lit.',
        'اختر حقل أسر علبة التوزيع. ملء الكابل يقرأه.',
    )
    add(
        '请选择光缆户数写入字段。',
        'Choose el campo donde el cable escribe los households.',
        'Elija el campo donde el cable escribe los hogares.',
        'Choisissez le champ où le câble écrit les foyers.',
        'اختر حقل كتابة أسر الكابل.',
    )
    add(
        '请选择用户点图层。',
        'Choose la layer de points de usuario.',
        'Elija la capa de puntos de usuario.',
        'Choisissez la couche de points usager.',
        'اختر طبقة نقاط المستخدم.',
    )
    add(
        '请选择皮线图层。',
        'Choose la layer de drop.',
        'Elija la capa de acometida.',
        'Choisissez la couche de branchement.',
        'اختر طبقة كبل الإسقاط.',
    )
    add(
        '请选择分纤盒写入字段。',
        'Choose el campo de escritura de la FAT box.',
        'Elija el campo de escritura de la caja FAT.',
        "Choisissez le champ d'écriture du FAT.",
        'اختر حقل كتابة علبة التوزيع.',
    )
    add(
        '请选择皮线户数字段。',
        'Choose el campo de households de la drop.',
        'Elija el campo de hogares de la acometida.',
        'Choisissez le champ foyers du branchement.',
        'اختر حقل أسر كبل الإسقاط.',
    )
    add(
        '请选择用户户数字段。',
        'Choose el campo de households del usuario.',
        'Elija el campo de hogares del usuario.',
        "Choisissez le champ foyers de l'usager.",
        'اختر حقل أسر المستخدم.',
    )
    add(
        '皮线两端都是分纤盒：{}',
        'Los dos extremos de la drop son FAT boxes: {}',
        'Los dos extremos de la acometida son cajas FAT: {}',
        'Les deux extremites du branchement sont des boitiers FAT : {}',
        'طرفا كبل الإسقاط علبتا توزيع: {}',
    )
    add(
        '皮线户数（每条写 1',
        'Households de drop (escribir 1 por cada una',
        'Hogares de acometida (escribir 1 por cada una',
        'Foyers de branchement (ecrire 1 pour chacun',
        'مشتركو كبل الإسقاط (كتابة 1 لكل واحد',
    )
    add(
        '皮线户数（抄用户户数',
        'Households de drop (copiar households de usuario',
        'Hogares de acometida (copiar hogares de usuario',
        'Foyers de branchement (copier les foyers abonnes',
        'مشتركو كبل الإسقاط (نسخ مشتركي المستخدم',
    )
    add(
        '；多盒覆盖也写 / 重复皮线跳过）',
        '; la cobertura de varias FAT boxes se escribe / las drops repetidas se omiten)',
        '; la cobertura de varias cajas FAT se escribe / las acometidas repetidas se omiten)',
        '; la couverture par plusieurs boitiers FAT est ecrite / les branchements en double sont ignores)',
        '; تُكتب تغطية عدة علب / تُتجاوز كبلات الإسقاط المكررة)',
    )
    add(
        '；已跳过多分纤盒覆盖 / 重复皮线）',
        '; se omitieron la cobertura de varias FAT boxes y las drops repetidas)',
        '; se omitieron la cobertura de varias cajas FAT y las acometidas repetidas)',
        '; couverture par plusieurs boitiers FAT et branchements en double ignores)',
        '; تُجاوزت تغطية عدة علب وكبلات الإسقاط المكررة)',
    )
    add(
        '光交图层筛选后没有可用点。',
        'La layer del cabinet no tiene points útiles tras el filter.',
        'La capa del armario no tiene puntos útiles tras el filtro.',
        "La couche de l'armoire n'a aucun point utilisable après le filtre.",
        'طبقة الكابينة بلا نقاط صالحة بعد التصفية.',
    )
    add(
        '分纤盒图层筛选后没有可用点。',
        'La layer de FAT boxes no tiene points utiles tras el filter.',
        'La capa de cajas FAT no tiene puntos utiles tras el filtro.',
        "La couche de boitiers FAT n'a aucun point utilisable apres filtrage.",
        'طبقة علب التوزيع لا تحوي نقاطًا صالحة بعد التصفية.',
    )
    add(
        '光缆图层筛选后没有可用线。',
        'La layer de cable no tiene lineas utiles tras el filter.',
        'La capa de cable no tiene lineas utiles tras el filtro.',
        "La couche de cable n'a aucune ligne utilisable apres filtrage.",
        'طبقة الكبل لا تحوي خطوطًا صالحة بعد التصفية.',
    )
    add(
        '  （无出线）',
        '  (sin cable de salida)',
        '  (sin cable de salida)',
        '  (pas de câble sortant)',
        '  (بلا كابل خارج)',
    )
    add(
        '用户图层筛选后没有可用点。',
        'La layer de usuarios no tiene points utiles tras el filter.',
        'La capa de usuarios no tiene puntos utiles tras el filtro.',
        "La couche d'abonnes n'a aucun point utilisable apres filtrage.",
        'طبقة المستخدمين لا تحوي نقاطًا صالحة بعد التصفية.',
    )
    add(
        '皮线图层筛选后没有可用线。',
        'La layer de drops no tiene lineas utiles tras el filter.',
        'La capa de acometidas no tiene lineas utiles tras el filtro.',
        "La couche de branchements n'a aucune ligne utilisable apres filtrage.",
        'طبقة كبل الإسقاط لا تحوي خطوطًا صالحة بعد التصفية.',
    )
    add(
        '皮线两端都是用户：{}',
        'Los dos extremos de la drop son usuarios: {}',
        'Los dos extremos de la acometida son usuarios: {}',
        'Les deux extremites du branchement sont des abonnes : {}',
        'طرفا كبل الإسقاط مستخدمان: {}',
    )
    add(
        '用户被 {} 个分纤盒覆盖，仍各写一条：{}（{}）',
        'Usuario cubierto por {} FAT boxes; aun se escribe una fila por cada una: {} ({})',
        'Usuario cubierto por {} cajas FAT; aun se escribe una fila por cada una: {} ({})',
        'Abonne couvert par {} boitiers FAT ; une ligne est tout de meme ecrite pour chacun : {} ({})',
        'مستخدم تغطيه {} علب توزيع، وتُكتب سطر لكل واحدة: {} ({})',
    )
    add(
        '用户被 {} 个分纤盒覆盖，不赋值：{}（{}）',
        'Usuario cubierto por {} FAT boxes, no se escribe: {} ({})',
        'Usuario cubierto por {} cajas FAT, no se escribe: {} ({})',
        'Abonne couvert par {} boitiers FAT, non ecrit : {} ({})',
        'مستخدم تغطيه {} علب توزيع، بدون كتابة: {} ({})',
    )
    add(
        '分纤盒户数（按所出皮线条数）',
        'Households de la FAT box (numero de drops de salida)',
        'Hogares de la caja FAT (numero de acometidas de salida)',
        'Foyers du boitier FAT (nombre de branchements sortants)',
        'مشتركو علبة التوزيع (عدد كبلات الإسقاط الخارجة)',
    )
    add(
        '分纤盒户数（按所出皮线字段合计）',
        'Households de la FAT box (suma de los campos de drop de salida)',
        'Hogares de la caja FAT (suma de los campos de acometida de salida)',
        'Foyers du boitier FAT (somme des champs de branchement sortants)',
        'مشتركو علبة التوزيع (مجموع حقول كبل الإسقاط الخارج)',
    )
    add(
        '终点歧义',
        'Extremo end ambiguo',
        'Extremo final ambiguo',
        'Extremite de fin ambigue',
        'النهاية ملتبسة',
    )
    add(
        '终点空',
        'Extremo end libre',
        'Extremo final libre',
        'Extremite de fin libre',
        'النهاية فارغة',
    )
    add(
        '另一头是分纤盒',
        'El otro extremo es una FAT box',
        'El otro extremo es una caja FAT',
        "L'autre extremite est un boitier FAT",
        'الطرف الآخر علبة توزيع',
    )
    add(
        '皮线一端空：{}',
        'La drop tiene un extremo libre: {}',
        'La acometida tiene un extremo libre: {}',
        'Le branchement a une extremite libre : {}',
        'كبل الإسقاط أحد طرفيه فارغ: {}',
    )
    add(
        '皮线两端都空：{}',
        'Los dos extremos de la drop estan libres: {}',
        'Los dos extremos de la acometida estan libres: {}',
        'Les deux extremites du branchement sont libres : {}',
        'طرفا كبل الإسقاط فارغان: {}',
    )
    add(
        '用户点总户数 {} 与皮线字段总户数 {} 不一致，请先检查皮线值。',
        'Los households de los points de usuario {} no coinciden con los {} del campo de drop. Revise primero los valores de drop.',
        'Los hogares de los puntos de usuario {} no coinciden con los {} del campo de acometida. Revise primero los valores de acometida.',
        "Les foyers des points abonnes {} ne correspondent pas aux {} du champ de branchement. Verifiez d'abord les valeurs de branchement.",
        'عدد مشتركي نقاط المستخدم {} لا يطابق {} في حقل كبل الإسقاط. افحص قيم كبل الإسقاط أولاً.',
    )
    add(
        '用户点总户数 {}，皮线字段总户数 {}。',
        'Households de points de usuario {}, households del campo de drop {}.',
        'Hogares de puntos de usuario {}, hogares del campo de acometida {}.',
        'Foyers des points abonnes {}, foyers du champ de branchement {}.',
        'مشتركو نقاط المستخدم {}، مشتركو حقل كبل الإسقاط {}.',
    )
    add(
        '两端接到{}',
        'Los dos extremos llegan a {}',
        'Los dos extremos llegan a {}',
        'Les deux extremites aboutissent a {}',
        'الطرفان يصلان إلى {}',
    )
    add(
        '另一头是{}',
        'El otro extremo es {}',
        'El otro extremo es {}',
        "L'autre extremite est {}",
        'الطرف الآخر هو {}',
    )
    add(
        '起点歧义',
        'Extremo inicial ambiguo',
        'Extremo inicial ambiguo',
        'Extremite de depart ambigue',
        'البداية ملتبسة',
    )
    add(
        '起点空',
        'Extremo inicial libre',
        'Extremo inicial libre',
        'Extremite de depart libre',
        'البداية فارغة',
    )
    add(
        '户数字段「{}」不在分纤盒图层：{}',
        'El campo de households «{}» no está en la layer de la FAT box: {}',
        'El campo de hogares «{}» no está en la capa de la caja FAT: {}',
        "Le champ foyers « {} » n'est pas sur la couche FAT : {}",
        'حقل الأسر «{}» ليس في طبقة علبة التوزيع: {}',
    )
    add(
        '光缆户数写入字段「{}」不在图层：{}',
        'El campo de escritura de households del cable «{}» no está en la layer: {}',
        'El campo de escritura de hogares del cable «{}» no está en la capa: {}',
        "Le champ d'écriture des foyers du câble « {} » n'est pas sur la couche : {}",
        'حقل كتابة أسر الكابل «{}» ليس في الطبقة: {}',
    )
    add(
        '分纤盒写入字段「{}」不在图层：{}',
        'El campo de escritura de la FAT box «{}» no está en la layer: {}',
        'El campo de escritura de la caja FAT «{}» no está en la capa: {}',
        "Le champ d'écriture du FAT « {} » n'est pas sur la couche : {}",
        'حقل كتابة علبة التوزيع «{}» ليس في الطبقة: {}',
    )
    add(
        '用户户数字段「{}」不在图层：{}',
        'El campo de households del usuario «{}» no está en la layer: {}',
        'El campo de hogares del usuario «{}» no está en la capa: {}',
        "Le champ foyers usager « {} » n'est pas sur la couche : {}",
        'حقل أسر المستخدم «{}» ليس في الطبقة: {}',
    )
    add(
        '皮线户数字段「{}」不在图层：{}',
        'El campo de households de la drop «{}» no está en la layer: {}',
        'El campo de hogares de la acometida «{}» no está en la capa: {}',
        "Le champ foyers du branchement « {} » n'est pas sur la couche : {}",
        'حقل أسر كبل الإسقاط «{}» ليس في الطبقة: {}',
    )
    add(
        '未写入。',
        'No escrito.',
        'No escrito.',
        'Non ecrit.',
        'لم يُكتب.',
    )
    add(
        '皮线字段总户数 {} 里有 {} 没有归到唯一分纤盒。',
        'De {} households del campo de drop, {} no quedan en una sola FAT box.',
        'De {} hogares del campo de acometida, {} no quedan en una sola caja FAT.',
        'Sur {} foyers du champ de branchement, {} ne sont pas rattaches a un seul boitier FAT.',
        'من {} مشترك في حقل كبل الإسقاط، {} غير مرتبط بعلبة توزيع واحدة.',
    )
    add(
        '  {} = {}（皮线 {} 条）',
        '  {} = {} ({} drops)',
        '  {} = {} ({} acometidas)',
        '  {} = {} ({} branchements)',
        '  {} = {} ({} كبلات إسقاط)',
    )
    add(
        '两端歧义',
        'Los dos extremos son ambiguos',
        'Los dos extremos son ambiguos',
        'Les deux extremites sont ambigues',
        'الطرفان ملتبسان',
    )
    add(
        '两端都空',
        'Los dos extremos estan libres',
        'Los dos extremos estan libres',
        'Les deux extremites sont libres',
        'الطرفان فارغان',
    )
    add(
        '另一头是分纤盒{}',
        'El otro extremo es la FAT box {}',
        'El otro extremo es la caja FAT {}',
        "L'autre extremite est le boitier FAT {}",
        'الطرف الآخر علبة التوزيع {}',
    )
    add(
        '分纤盒户数为 0 或空：{}',
        'Los households de la FAT box son 0 o estan vacios: {}',
        'Los hogares de la caja FAT son 0 o estan vacios: {}',
        'Le nombre de foyers du boitier FAT est 0 ou vide : {}',
        'عدد مشتركي علبة التوزيع صفر أو فارغ: {}',
    )
    add(
        '配置图层筛选后无要素：{}（{}）',
        'La layer configurada no tiene features tras el filter: {} ({})',
        'La capa configurada no tiene elementos tras el filtro: {} ({})',
        "La couche configuree n'a aucune entite apres filtrage : {} ({})",
        'الطبقة المهيأة بلا عناصر بعد التصفية: {} ({})',
    )
    add(
        '{} CODE {} 已被图层 {} 里未重写的要素 #{} 占用：{}',
        '{} CODE {} ya lo usa en la layer {} el feature #{} que esta pasada no reescribio: {}',
        '{} CODE {} ya lo usa en la capa {} el elemento #{} que esta pasada no reescribio: {}',
        "{} CODE {} est deja pris sur la couche {} par l'entite #{} non reecrite : {}",
        '{} الرمز {} مستخدم في الطبقة {} لدى العنصر #{} الذي لم تُعد كتابته: {}',
    )
    add(
        '皮线两端接到同一点：{}',
        'Los dos extremos de la drop llegan al mismo point: {}',
        'Los dos extremos de la acometida llegan al mismo punto: {}',
        'Les deux extremites du branchement aboutissent au meme point : {}',
        'طرفا كبل الإسقاط يصلان إلى النقطة نفسها: {}',
    )
    add(
        '同一分纤盒到同一用户有 {} 条皮线，已剔除：{} ← {}',
        '{} drops de la misma FAT box al mismo usuario se descartaron: {} ← {}',
        '{} acometidas de la misma caja FAT al mismo usuario se descartaron: {} ← {}',
        '{} branchements du meme boitier FAT vers le meme abonne ont ete ecartes : {} ← {}',
        'أُزيلت {} كبلات إسقاط من علبة التوزيع نفسها إلى المستخدم نفسه: {} ← {}',
    )
    add(
        '不赋值。请先检查皮线。',
        'No se escribio nada. Revise primero las drops.',
        'No se escribio nada. Revise primero las acometidas.',
        "Rien n'a ete ecrit. Verifiez d'abord les branchements.",
        'لم يُكتب شيء. افحص كبلات الإسقاط أولاً.',
    )
    add(
        '起点是{}',
        'El extremo inicial es {}',
        'El extremo inicial es {}',
        "L'extremite de depart est {}",
        'البداية هي {}',
    )
    add(
        '终点是{}',
        'El extremo end es {}',
        'El extremo final es {}',
        "L'extremite de fin est {}",
        'النهاية هي {}',
    )
    add(
        '分纤盒{}',
        'FAT box {}',
        'Caja FAT {}',
        'Boitier FAT {}',
        'علبة توزيع {}',
    )
    add(
        '配置图层未有效参与：{}（{}，筛选 {} 个）',
        'La layer configurada no participo de verdad: {} ({}, {} tras el filter)',
        'La capa configurada no participo de verdad: {} ({}, {} tras el filtro)',
        "La couche configuree n'a pas vraiment participe : {} ({}, {} apres filtrage)",
        'الطبقة المهيأة لم تشارك فعليًا: {} ({}, {} بعد التصفية)',
    )
    add(
        '字段「{}」（图层 {}）不是文本类型，写不进 CODE。',
        'El campo "{}" de la layer {} no es de texto, no se puede escribir el CODE.',
        'El campo "{}" de la capa {} no es de texto, no se puede escribir el CODE.',
        'Le champ "{}" de la couche {} n\'est pas du texte, le CODE ne peut pas y etre ecrit.',
        'الحقل "{}" في الطبقة {} ليس نصًا، فلا يمكن كتابة CODE.',
    )
    add(
        '字段「{}」（图层 {}）长度 {}，CODE 最长 {} 个字符，保存时会被截断。请先加宽字段。',
        'El campo "{}" de la layer {} tiene longitud {}, pero el CODE mas largo tiene {} caracteres y se cortaria al guardar. Amplie el campo primero.',
        'El campo "{}" de la capa {} tiene longitud {}, pero el CODE mas largo tiene {} caracteres y se cortaria al guardar. Amplie el campo primero.',
        'Le champ "{}" de la couche {} a une longueur de {}, mais le CODE le plus long a {} caracteres et serait coupe a l\'enregistrement. Elargissez le champ d\'abord.',
        'الحقل "{}" في الطبقة {} طوله {}، وأطول CODE هو {} محرفًا وسيُقص عند الحفظ. وسّع الحقل أولاً.',
    )
    add(
        '皮线{}同时靠近多个点：{}',
        'La drop {} esta cerca de varios points: {}',
        'La acometida {} esta cerca de varios puntos: {}',
        'Le branchement {} est proche de plusieurs points : {}',
        'كبل الإسقاط {} قريب من عدة نقاط: {}',
    )
    add(
        '未挂上：{}',
        'No conectado: {}',
        'No conectado: {}',
        'Non rattache : {}',
        'غير موصول: {}',
    )
    add(
        '成环：{}',
        'Bucle: {}',
        'Bucle: {}',
        'Boucle : {}',
        'حلقة: {}',
    )
    add(
        '分纤盒进入 {} 条线：{}',
        'La FAT box tiene {} lineas de entrada: {}',
        'La caja FAT tiene {} lineas de entrada: {}',
        'Le boitier FAT a {} lignes entrantes : {}',
        'علبة التوزيع لها {} خطوط داخلة: {}',
    )
    add(
        '分纤盒分叉（出 {} 条线）：{}',
        'Ramal de FAT box ({} lineas de salida): {}',
        'Ramal de caja FAT ({} lineas de salida): {}',
        'Branchement de boitier FAT ({} lignes sortantes) : {}',
        'تفرع علبة التوزيع ({} خطوط خارجة): {}',
    )
    add(
        '接头进入 {} 条线：{}',
        'El splice tiene {} lineas de entrada: {}',
        'El empalme tiene {} lineas de entrada: {}',
        "L'epissure a {} lignes entrantes : {}",
        'المفصل له {} خطوط داخلة: {}',
    )
    add(
        '光交被当作下游：{}',
        'Cabinet tratado como downstream: {}',
        'Armario tratado como aguas abajo: {}',
        'Armoire traitee comme aval : {}',
        'كابينة عُوملت كجهة لاحقة: {}',
    )
    add(
        '光交没有出线：{}',
        'El cabinet no tiene cable de salida: {}',
        'El armario no tiene cable de salida: {}',
        "L'armoire n'a pas de câble sortant : {}",
        'الكابينة بلا كابل خارج: {}',
    )
    add(
        '两端都空：{}',
        'Los dos extremos estan libres: {}',
        'Los dos extremos estan libres: {}',
        'Les deux extremites sont libres : {}',
        'الطرفان فارغان: {}',
    )
    add(
        '一端空：{}',
        'Un extremo está empty: {}',
        'Un extremo está vacío: {}',
        'Une extrémité est vide : {}',
        'طرف واحد فارغ: {}',
    )
    add(
        '线两端接到同一点：{}',
        'Los dos extremos de la line se ajustan al mismo point: {}',
        'Los dos extremos de la línea se ajustan al mismo punto: {}',
        "Les deux extrémités de la ligne s'accrochent au même point : {}",
        'طرفا الخط يلتقطان النقطة نفسها: {}',
    )
    add(
        '未挂上（未从光交通到）：{}',
        'No conectado (no se alcanza desde un cabinet): {}',
        'No conectado (no se alcanza desde un armario): {}',
        'Non rattache (non atteint depuis une armoire) : {}',
        'غير موصول (لم يُبلغ من كابينة): {}',
    )
    add(
        '成环：{} ↔ {}',
        'Bucle: {} ↔ {}',
        'Bucle: {} ↔ {}',
        'Boucle : {} ↔ {}',
        'حلقة: {} ↔ {}',
    )
    add(
        '请选择一个矢量图层',
        'Seleccione una layer vectorial',
        'Seleccione una capa vectorial',
        'Choisissez une couche vecteur',
        'اختر طبقة متجهة',
    )
    add(
        '当前图层没有符号化',
        'La layer actual no tiene symbology',
        'La capa actual no tiene simbología',
        "La couche actuelle n'a pas de symbologie",
        'الطبقة الحالية بلا ترميز',
    )
    add(
        '当前符号化没有可勾选的分组',
        'La symbology no tiene un grupo que se pueda marcar',
        'La simbología no tiene un grupo que se pueda marcar',
        "La symbologie n'a aucun groupe à cocher",
        'الترميز بلا مجموعة يمكن تعليمها',
    )
    add(
        '当前符号化不是分类/规则（%s），没有可筛选的分组',
        'La symbology no es por categories ni por reglas (%s), así que there are no un grupo que filter',
        'La simbología no es por categorías ni por reglas (%s), así que no hay un grupo que filtrar',
        "La symbologie n'est ni catégorisée ni par règles (%s), donc aucun groupe à filtrer",
        'الترميز ليس تصنيفًا ولا قواعد (%s)، لذلك لا توجد مجموعة للتصفية',
    )
    add(
        '读取分类失败：%s',
        'No se pudieron leer las clases: %s',
        'No se pudieron leer las clases: %s',
        'Impossible de lire les classes : %s',
        'تعذرت قراءة الفئات: %s',
    )
    add(
        '正在检查线端',
        'Checking extremos',
        'Comprobando extremos',
        'Contrôle des extrémités',
        'فحص أطراف الخط',
    )
    add(
        '从光交往外走，数字化起点应在上游。',
        'Al salir del cabinet, el start digitalizado debe quedar upstream.',
        'Al salir del armario, el inicio digitalizado debe quedar aguas arriba.',
        "En partant de l'armoire vers l'extérieur, le départ numérisé doit être en amont.",
        'عند السير من الكابينة إلى الخارج، يجب أن تكون البداية المرقمنة في المنبع.',
    )
    add(
        '修复只改线的顶点顺序，不改属性；写入编辑缓冲，需要你自己保存图层。',
        'Fix only reorders line vertices, not attributes; it writes the edit buffer — save the layer yourself.',
        'La reparación solo invierte el orden de los vértices. Los atributos no cambian. Escribe en el búfer de edición; guarde usted la capa.',
        "La réparation inverse seulement l'ordre des sommets. Les attributs restent. Elle écrit dans le tampon d'édition ; enregistrez la couche vous-même.",
        'الإصلاح يقلب ترتيب الرؤوس فقط ولا يغيّر الخصائص. يكتب في مخزن التحرير؛ احفظ الطبقة بنفسك.',
    )
    add(
        '建议：',
        'Tip:',
        'Sugerencia:',
        'Suggestion :',
        'اقتراح:',
    )
    add(
        'NTAL 线方向修复',
        'Repair de la direction de lines',
        'Reparación de la dirección de líneas',
        'Réparation du sens des lignes',
        'إصلاح اتجاه الخطوط',
    )
    add(
        '正在检查…',
        'Checking…',
        'Comprobando…',
        'Contrôle…',
        'جارٍ الفحص…',
    )
    add(
        '请在图层配置里选择光交。方向从光交往外走。',
        'Choose la layer del cabinet en la setup. La direction sale del cabinet hacia fuera.',
        'Elija la capa del armario en la configuración. La dirección sale del armario hacia fuera.',
        "Choisissez la couche d'armoire dans la configuration. Le sens part de l'armoire vers l'extérieur.",
        'اختر طبقة الكابينة في إعداد الطبقات. الاتجاه يسير من الكابينة إلى الخارج.',
    )
    add(
        '请至少配置光缆或皮线其中一类。',
        'Configure al menos el cable o la drop.',
        'Configure al menos el cable o la acometida.',
        'Configurez au moins le câble ou le branchement.',
        'اضبط الكابل أو كبل الإسقاط على الأقل.',
    )
    add(
        '正在读取点',
        'Reading points',
        'Leyendo puntos',
        'Lecture des points',
        'قراءة النقاط',
    )
    add(
        '正在读取线',
        'Reading lines',
        'Leyendo líneas',
        'Lecture des lignes',
        'قراءة الخطوط',
    )
    add(
        '正在检查网络结构',
        'Checking la estructura de la red',
        'Comprobando la estructura de la red',
        'Contrôle de la structure du réseau',
        'فحص بنية الشبكة',
    )
    add(
        '修完再用「线显示」看：圆点（起点）应更靠近光交一侧。',
        'Después de reparar, el point de start debe quedar más cerca del lado del cabinet.',
        'Después de reparar, el punto de inicio debe quedar más cerca del lado del armario.',
        "Après réparation, le point de départ doit être plus près du côté de l'armoire.",
        'بعد الإصلاح، يجب أن تكون نقطة البداية أقرب إلى جانب الكابينة.',
    )
    add(
        '从光交通到的线方向都正确。',
        'Todas las lines alcanzadas desde un cabinet ya apuntan bien.',
        'Todas las líneas alcanzadas desde un armario ya apuntan bien.',
        'Toutes les lignes atteintes depuis une armoire sont déjà dans le bon sens.',
        'كل الخطوط المبلوغة من كابينة تشير الاتجاه الصحيح.',
    )
    add(
        '不挡地图，窗口置顶。打勾的翻转，不打勾的不动。方向反了默认打勾，伪成环和方向无法判断默认不勾。',
        'Esta ventana queda encima y no tapa el mapa. Lo marcado se invierte; lo demás se queda. Las reversed empiezan checked. Los falsos loops y las direcciones sin decidir empiezan sin marcar.',
        'Esta ventana queda encima y no tapa el mapa. Lo marcado se invierte; lo demás se queda. Las invertidas empiezan marcadas. Los falsos bucles y las direcciones sin decidir empiezan sin marcar.',
        'Cette fenêtre reste au-dessus et ne bloque pas la carte. Le coché est inversé ; le reste reste. Les lignes inversées commencent cochées. Les fausses boucles et les sens indécis commencent décochés.',
        'هذه النافذة تبقى في الأعلى ولا تحجب الخريطة. المعلَّم يُقلب والباقي يبقى. المعكوس يبدأ معلَّمًا. الحلقة الكاذبة والاتجاه غير المحسوم يبدآن بلا علامة.',
    )
    add(
        '检查',
        'Check',
        'Comprobación',
        'Contrôle',
        'فحص',
    )
    add(
        '明细',
        'Detalle',
        'Detalle',
        'Détail',
        'تفصيل',
    )
    add(
        '可修复',
        'Fixable',
        'Reparable',
        'Réparable',
        'قابل للإصلاح',
    )
    add(
        '翻转勾选',
        'Reverse checked',
        'Invertir las marcadas',
        'Inverser les cochées',
        'قلب المعلَّم',
    )
    add(
        '关闭',
        'Close',
        'Cerrar',
        'Fermer',
        'إغلاق',
    )
    add(
        '<b>图层参与</b>（走到 / 筛出）',
        '<b>Layers usadas</b> (alcanzadas / filtradas)',
        '<b>Capas usadas</b> (alcanzadas / filtradas)',
        '<b>Couches utilisées</b> (atteintes / filtrées)',
        '<b>الطبقات المشاركة</b> (بُلغت / صُفّيت)',
    )
    add(
        '全部翻转',
        'Reverse all',
        'Invertir todas',
        'Tout inverser',
        'قلب الكل',
    )
    add(
        '正在生成临时图层',
        'Creating temporary layers',
        'Creando capas temporales',
        'Création des couches temporaires',
        'إنشاء طبقات مؤقتة',
    )
    add(
        '没有可用的线。',
        'There are no una line útil.',
        'No hay una línea útil.',
        "Il n'y a aucune ligne utilisable.",
        'لا يوجد خط صالح.',
    )
    add(
        '容差 {} 米。',
        'Tolerance {} m.',
        'Tolerancia {} m.',
        'Tolérance {} m.',
        'السماحية {} م.',
    )
    add(
        '。多段线会整条一起倒转。',
        ' Las lines multiparte se invierten enteras.',
        ' Las líneas multiparte se invierten enteras.',
        " Les lignes multi-parties sont inversées d'un bloc.",
        ' الخط متعدد الأجزاء يُقلب كله معًا.',
    )
    add(
        '方向反了 {} 条：数字化终点在上游。可用「全部翻转」，或在表里勾选后「翻转勾选」。',
        '{} lines están reversed: el end digitalizado está upstream. Use Reverse all, o marque filas y use Reverse checked.',
        '{} líneas están invertidas: el final digitalizado está aguas arriba. Use Invertir todas, o marque filas y use Invertir marcadas.',
        '{} lignes sont inversées : la fin numérisée est en amont. Utilisez Tout inverser, ou cochez des lignes puis Inverser la sélection.',
        '{} خطوط معكوسة: النهاية المرقمنة في المنبع. استخدم قلب الكل، أو علّم صفوفًا ثم قلب المعلَّم.',
    )
    add(
        '检查了线 {} 条（光缆 {}，其中主干 {}、配线 {}，皮线 {}）。',
        'Se comprobaron {} lines (cable {}, de ellas feeder {}, distribution {}, drop {}).',
        'Se comprobaron {} líneas (cable {}, de ellas alimentador {}, distribución {}, acometida {}).',
        '{} lignes contrôlées (câble {}, dont alimentation {}, distribution {}, branchement {}).',
        'فُحصت {} خطوط (كابل {}، منها تغذية {}، توزيع {}، إسقاط {}).',
    )
    add(
        '从光交通到 {} 条，方向正确 {} 条，方向反了 {} 条。',
        'Alcanzadas {} desde un cabinet: {} correct, {} reversed.',
        'Alcanzadas {} desde un armario: {} correctas, {} invertidas.',
        '{} atteintes depuis une armoire : {} dans le bon sens, {} inversées.',
        'بُلغ {} من كابينة: {} صحيحة، {} معكوسة.',
    )
    add(
        '风险：硬错误 {}，软错误 {}，警告 {}（含方向反了）。',
        'Riesgo: {} hard errors, {} leves, {} warnings (incluye direction reversed).',
        'Riesgo: {} errores duros, {} leves, {} avisos (incluye dirección invertida).',
        'Risque : {} erreurs dures, {} souples, {} avertissements (sens inversé compris).',
        'الخطر: أخطاء صارمة {}، مرنة {}، تحذيرات {} (تشمل الاتجاه المعكوس).',
    )
    add(
        '结构硬错误 {} 处（成环、分叉、多进线、光交被当成下游），不参与翻转。',
        '{} hard errors de estructura (loops, ramales, varias entradas, cabinet tratado como downstream) no se invierten.',
        '{} errores duros de estructura (bucles, ramales, varias entradas, armario tratado como aguas abajo) no se invierten.',
        '{} erreurs dures de structure (boucles, branches, entrées multiples, armoire traitée comme aval) ne sont pas inversées.',
        '{} أخطاء بنية صارمة (حلقات، تفرعات، عدة خطوط داخلة، كابينة تُعامل كمصب) لا تُقلب.',
    )
    add(
        '不挡地图，窗口置顶。检查页是这次的硬错误、软错误和警告；可修复页是方向反了的线。全部翻转=这些线一次翻；翻转勾选=只翻表里打勾的。',
        'Esta ventana queda encima y no tapa el mapa. La página Comprobar lista hard errors, leves y warnings. Fixable lista las lines reversed. Reverse all las invierte de una vez. Reverse checked invierte solo las filas checked.',
        'Esta ventana queda encima y no tapa el mapa. La página Comprobar lista errores duros, leves y avisos. Reparable lista las líneas invertidas. Invertir todas las invierte de una vez. Invertir marcadas invierte solo las filas marcadas.',
        "Cette fenêtre reste au-dessus et ne bloque pas la carte. La page Contrôle liste les erreurs dures, souples et les avertissements. Réparable liste les lignes inversées. Tout inverser les inverse d'un coup. Inverser la sélection n'inverse que les lignes cochées.",
        'هذه النافذة تبقى في الأعلى ولا تحجب الخريطة. صفحة الفحص تسرد الأخطاء الصارمة والمرنة والتحذيرات. القابل للإصلاح يسرد الخطوط المعكوسة. قلب الكل يقلبها دفعة واحدة. قلب المعلَّم يقلب الصفوف المعلَّمة فقط.',
    )
    add(
        '不挡地图，窗口置顶。全部翻转=所有方向反了的线；翻转勾选=只翻表里打勾的。',
        'Esta ventana queda encima y no tapa el mapa. Reverse all invierte cada line reversed. Reverse checked invierte solo las filas checked.',
        'Esta ventana queda encima y no tapa el mapa. Invertir todas invierte cada línea invertida. Invertir marcadas invierte solo las filas marcadas.',
        "Cette fenêtre reste au-dessus et ne bloque pas la carte. Tout inverser inverse chaque ligne inversée. Inverser la sélection n'inverse que les lignes cochées.",
        'هذه النافذة تبقى في الأعلى ولا تحجب الخريطة. قلب الكل يقلب كل خط معكوس. قلب المعلَّم يقلب الصفوف المعلَّمة فقط.',
    )
    add(
        '修',
        'Corregir',
        'Corregir',
        'Corriger',
        'إصلاح',
    )
    add(
        '类型',
        'Tipo',
        'Tipo',
        'Type',
        'النوع',
    )
    add(
        '名称',
        'Nombre',
        'Nombre',
        'Nom',
        'الاسم',
    )
    add(
        '说明',
        'Detail',
        'Nota',
        'Note',
        'ملاحظة',
    )
    add(
        '不管表格勾选，把检查到的全部「方向反了」的线一次翻转。',
        'Invierte todas las lines halladas reversed, estén o no checked.',
        'Invierte todas las líneas halladas invertidas, estén o no marcadas.',
        'Inverse toutes les lignes trouvées inversées, cochées ou non.',
        'يقلب كل خط وُجد معكوسًا، سواء كان معلَّمًا أم لا.',
    )
    add(
        '只翻转打勾的线。方向反了默认打勾，伪成环和方向无法判断默认不勾。',
        'Invierte solo las lines checked. Las reversed empiezan checked. Los falsos loops y las direcciones sin decidir empiezan sin marcar.',
        'Invierte solo las líneas marcadas. Las invertidas empiezan marcadas. Los falsos bucles y las direcciones sin decidir empiezan sin marcar.',
        'Inverse seulement les lignes cochées. Les lignes inversées commencent cochées. Les fausses boucles et les sens indécis commencent décochés.',
        'يقلب الخطوط المعلَّمة فقط. المعكوسة تبدأ معلَّمة. الحلقات الكاذبة والاتجاهات غير المحسومة تبدأ بلا علامة.',
    )
    add(
        '只翻转「可修复」表里打勾的线，可先对照地图去掉不确定的。',
        'Invierte solo las filas checked en Fixable. Desmarque en el mapa lo que no esté seguro.',
        'Invierte solo las filas marcadas en Reparable. Desmarque en el mapa lo que no esté seguro.',
        "Inverse seulement les lignes cochées dans Réparable. Décochez d'abord sur la carte ce dont vous n'êtes pas sûr.",
        'يقلب الصفوف المعلَّمة في القابل للإصلاح فقط. أزل علامة ما لست متأكدًا منه على الخريطة أولًا.',
    )
    add(
        '<span style="color:#c62828; font-weight:700;">配置</span>',
        '<span style="color:#c62828; font-weight:700;">Setup</span>',
        '<span style="color:#c62828; font-weight:700;">Configuración</span>',
        '<span style="color:#c62828; font-weight:700;">Configuration</span>',
        '<span style="color:#c62828; font-weight:700;">الإعداد</span>',
    )
    add(
        '问题点在图层组「全面检测」里，下面分「硬错误」「软错误」「警告」。关掉本窗后图层还在，双击「可修复」表可缩放到对应点。',
        'Los points están en el grupo Full check, separados en hard errors, leves y warnings. Siguen ahí al cerrar esta ventana. Pulse dos veces una fila de Fixable para acercarse.',
        'Los puntos están en el grupo Comprobación completa, separados en errores duros, leves y avisos. Siguen ahí al cerrar esta ventana. Pulse dos veces una fila de Reparable para acercarse.',
        'Les points sont dans le groupe Contrôle complet, séparés en erreurs dures, souples et avertissements. Ils restent après la fermeture. Double-cliquez une ligne Réparable pour zoomer.',
        'النقاط في مجموعة الفحص الكامل، مقسمة إلى أخطاء صارمة ومرنة وتحذيرات. تبقى بعد إغلاق النافذة. انقر مرتين صفًا قابلًا للإصلاح للتكبير.',
    )
    add(
        '问题点已写入图层组「拓扑检查结果」。默认只显示「线方向反了」，其余图层在该组里，需要时再勾选。',
        'Los points de problema se escribieron en el grupo Topology check. Al principio solo se ven las lines reversed. Las demás capas están en ese grupo.',
        'Los puntos de problema se escribieron en el grupo Comprobación topológica. Al principio solo se ven las líneas invertidas. Las demás capas están en ese grupo.',
        'Les points de problème sont dans le groupe Contrôle topologique. Seules les lignes inversées sont visibles au début. Les autres couches sont dans ce groupe.',
        'كُتبت نقاط المشكلة في مجموعة فحص الطوبولوجيا. في البداية تظهر الخطوط المعكوسة فقط. الطبقات الأخرى في تلك المجموعة.',
    )
    add(
        '\n已翻转 {} 条线到编辑缓冲。请保存图层。',
        '\nSe invirtieron {} lines en el edit buffer. Save la layer.',
        '\nSe invirtieron {} líneas en el búfer de edición. Guarde la capa.',
        "\n{} lignes inversées dans le tampon d'édition. Enregistrez la couche.",
        '\nقُلب {} خطوط إلى مخزن التحرير. احفظ الطبقة.',
    )
    add(
        '没有打勾的线。',
        'No lines are checked.',
        'No hay líneas marcadas.',
        "Aucune ligne n'est cochée.",
        'لا توجد خطوط معلَّمة.',
    )
    add(
        '线方向检查',
        'Line direction check',
        'Dirección de líneas',
        'Sens des lignes',
        'اتجاه الخطوط',
    )
    add(
        'NTAL 线方向',
        'Direction de lines',
        'Dirección de líneas',
        'Sens des lignes',
        'اتجاه الخطوط',
    )
    add(
        '已生成临时图层：',
        'Temporary layers created: ',
        'Capas temporales creadas:',
        'Couches temporaires créées :',
        'تم إنشاء طبقات مؤقتة:',
    )
    add(
        '数字化方向反了（终点在上游）：{}  上游 {}  下游 {}',
        'La direction digitalizada está reversed (el end está upstream): {}  upstream {}  downstream {}',
        'La dirección digitalizada está invertida (el final está aguas arriba): {}  aguas arriba {}  aguas abajo {}',
        'Le sens numérisé est inversé (la fin est en amont) : {}  amont {}  aval {}',
        'الاتجاه المرقمن معكوس (النهاية في المنبع): {}  المنبع {}  المصب {}',
    )
    add(
        '一端空/两端空 {} 处：建议先用「线显示」看端点，或把吸附容差改大一点。',
        '{} sitios tienen uno o los dos extremos empty. Muestre los extremos, o aumente la snap tolerance.',
        '{} sitios tienen uno o los dos extremos vacíos. Muestre los extremos, o aumente la tolerancia de ajuste.',
        "{} endroits ont une extrémité ou les deux vides. Affichez les extrémités, ou augmentez la tolérance d'accrochage.",
        '{} مواضع فيها طرف أو الطرفان فارغان. أظهر أطراف الخط، أو زِد سماحية الالتقاط.',
    )
    add(
        '未从光交通到 {} 条：可能断在接头/分纤盒，或图层没配齐。通不到的线程序不会翻。',
        '{} lines no se alcanzaron desde un cabinet. El corte puede estar en un splice o una FAT box, o falta una layer. Las lines no alcanzadas no se invierten.',
        '{} líneas no se alcanzaron desde un armario. El corte puede estar en un empalme o una caja FAT, o falta una capa. Las líneas no alcanzadas no se invierten.',
        '{} lignes non atteintes depuis une armoire. La coupure peut être à une épissure ou un FAT, ou une couche manque. Les lignes non atteintes ne sont pas inversées.',
        '{} خطوط لم تُبلَغ من كابينة. قد يكون القطع عند وصلة أو علبة توزيع، أو طبقة ناقصة. الخطوط غير المبلوغة لا تُقلب.',
    )
    add(
        '端点歧义 {} 处：容差内有多个点，先错开点或改小容差，否则方向不可靠。',
        '{} extremos ambiguos: hay varios points dentro de la tolerance. Sepárelos o baje la tolerance, o la direction no es fiable.',
        '{} extremos ambiguos: hay varios puntos dentro de la tolerancia. Sepárelos o baje la tolerancia, o la dirección no es fiable.',
        "{} extrémités ambiguës : plusieurs points sont dans la tolérance. Écartez-les ou baissez la tolérance, sinon le sens n'est pas fiable.",
        '{} أطراف ملتبسة: عدة نقاط داخل السماحية. باعدها أو خفّض السماحية، وإلا فالاتجاه غير موثوق.',
    )
    add(
        '自环 {} 处：线两端接到同一点，不会自动翻。',
        '{} loops propios: los dos extremos se ajustan al mismo point y no se invierten solos.',
        '{} bucles propios: los dos extremos se ajustan al mismo punto y no se invierten solos.',
        "{} boucles : les deux extrémités s'accrochent au même point et ne sont pas inversées.",
        '{} حلقات ذاتية: الطرفان يلتقطان النقطة نفسها ولا يُقلبان تلقائيًا.',
    )
    add(
        '结构硬错误 {} 处：成环、分叉、多进线或光交被当成下游。只报告，不翻转。',
        '{} hard errors de estructura: loops, ramales, varias entradas o un cabinet tratado como downstream. Solo se informan, no se invierten.',
        '{} errores duros de estructura: bucles, ramales, varias entradas o un armario tratado como aguas abajo. Solo se informan, no se invierten.',
        '{} erreurs dures de structure : boucles, branches, entrées multiples ou une armoire traitée comme aval. Signalées seulement, pas inversées.',
        '{} أخطاء بنية صارمة: حلقات أو تفرعات أو عدة خطوط داخلة أو كابينة تُعامل كمصب. تُبلَّغ فقط ولا تُقلب.',
    )
    add(
        '<b>全面检测</b>\u3000含线方向\u3000容差 {} 米<br>',
        '<b>Full check</b>\u3000incluye direction de lines\u3000tolerance {} m<br>',
        '<b>Comprobación completa</b>\u3000incluye dirección de líneas\u3000tolerancia {} m<br>',
        '<b>Contrôle complet</b>\u3000avec le sens des lignes\u3000tolérance {} m<br>',
        '<b>فحص كامل</b>\u3000يشمل اتجاه الخطوط\u3000السماحية {} م<br>',
    )
    add(
        '<div>（无）</div>',
        '<div>(none)</div>',
        '<div>(ninguno)</div>',
        '<div>(aucun)</div>',
        '<div>(لا شيء)</div>',
    )
    add(
        '将翻转全部 {} 条「方向反了」的线，不看勾选。\n只改顶点顺序，写入编辑缓冲，不保存。\n一端空、未挂上、歧义的线不会动。\n继续？',
        'Se invertirán las {} lines checked como reversed, sin mirar las casillas.\nSolo cambia el orden de los vertices, en el edit buffer, sin guardar.\nLas lines con un extremo empty, sueltas o ambiguas no se mueven.\n¿Continue?',
        'Se invertirán las {} líneas marcadas como invertidas, sin mirar las casillas.\nSolo cambia el orden de los vértices, en el búfer de edición, sin guardar.\nLas líneas con un extremo vacío, sueltas o ambiguas no se mueven.\n¿Continuar?',
        "Inverser les {} lignes marquées inversées, sans regarder les cases.\nSeul l'ordre des sommets change, dans le tampon d'édition, sans enregistrer.\nLes lignes à extrémité vide, non rattachées ou ambiguës ne bougent pas.\nContinuer ?",
        'سيُقلب كل الخطوط المعكوسة وعددها {}، دون النظر إلى العلامات.\nيتغير ترتيب الرؤوس فقط، في مخزن التحرير، بلا حفظ.\nالخطوط ذات طرف فارغ أو غير المعلقة أو الملتبسة لا تتحرك.\nهل تتابع؟',
    )
    add(
        '将翻转勾选的 {} 条线。\n只改顶点顺序，写入编辑缓冲，不保存。\n继续？',
        'Se invertirán las {} lines checked.\nSolo cambia el orden de los vertices, en el edit buffer, sin guardar.\n¿Continue?',
        'Se invertirán las {} líneas marcadas.\nSolo cambia el orden de los vértices, en el búfer de edición, sin guardar.\n¿Continuar?',
        "Inverser les {} lignes cochées.\nSeul l'ordre des sommets change, dans le tampon d'édition, sans enregistrer.\nContinuer ?",
        'سيُقلب {} خطوط معلَّمة.\nيتغير ترتيب الرؤوس فقط، في مخزن التحرير، بلا حفظ.\nهل تتابع؟',
    )
    add(
        '  正向  {}  {} → {}',
        '  correct  {}  {} → {}',
        '  correcto  {}  {} → {}',
        '  bon sens  {}  {} → {}',
        '  صحيح  {}  {} → {}',
    )
    add(
        '  反了  {}',
        '  reversed  {}',
        '  invertido  {}',
        '  inversé  {}',
        '  معكوس  {}',
    )
    add(
        '  {}：正向 {}，反了 {}。',
        '  {}: correct {}, reversed {}.',
        '  {}: correcto {}, invertido {}.',
        '  {} : bon sens {}, inversé {}.',
        '  {}: صحيح {}، معكوس {}.',
    )
    add(
        '<span style="color:#c62828; font-weight:700;">错误（未到达起点）：{}</span>',
        '<span style="color:#c62828; font-weight:700;">Errores (inalcanzables desde un start): {}</span>',
        '<span style="color:#c62828; font-weight:700;">Errores (inalcanzables desde un inicio): {}</span>',
        '<span style="color:#c62828; font-weight:700;">Erreurs (inatteignables depuis un départ) : {}</span>',
        '<span style="color:#c62828; font-weight:700;">أخطاء (لا تُبلغ من بداية): {}</span>',
    )
    add(
        '<br><span style="color:#c62828; font-weight:700;">硬错误：{}</span>',
        '<br><span style="color:#c62828; font-weight:700;">Hard errors: {}</span>',
        '<br><span style="color:#c62828; font-weight:700;">Errores duros: {}</span>',
        '<br><span style="color:#c62828; font-weight:700;">Erreurs dures : {}</span>',
        '<br><span style="color:#c62828; font-weight:700;">أخطاء صارمة: {}</span>',
    )
    add(
        '<span style="color:#ef6c00; font-weight:700;">软错误：{}</span>',
        '<span style="color:#ef6c00; font-weight:700;">Soft errors: {}</span>',
        '<span style="color:#ef6c00; font-weight:700;">Errores leves: {}</span>',
        '<span style="color:#ef6c00; font-weight:700;">Erreurs souples : {}</span>',
        '<span style="color:#ef6c00; font-weight:700;">أخطاء مرنة: {}</span>',
    )
    add(
        '<span style="color:#f9a825; font-weight:700;">警告：{}</span>',
        '<span style="color:#f9a825; font-weight:700;">Warnings: {}</span>',
        '<span style="color:#f9a825; font-weight:700;">Avisos: {}</span>',
        '<span style="color:#f9a825; font-weight:700;">Avertissements : {}</span>',
        '<span style="color:#f9a825; font-weight:700;">تحذيرات: {}</span>',
    )
    add(
        '{} 无法进入编辑',
        '{} no puede empezar a editarse',
        '{} no puede empezar a editarse',
        '{} ne peut pas passer en édition',
        '{} لا يمكن بدء تحريره',
    )
    add(
        '{} 修复异常：{}',
        '{} error de repair: {}',
        '{} error de reparación: {}',
        '{} erreur de réparation : {}',
        '{} خطأ في الإصلاح: {}',
    )
    add(
        '起点同时靠近多个点：{}',
        'El start está dentro de la tolerance de varios points: {}',
        'El inicio está dentro de la tolerancia de varios puntos: {}',
        'Le départ est à portée de tolérance de plusieurs points : {}',
        'البداية ضمن السماحية من عدة نقاط: {}',
    )
    add(
        '终点同时靠近多个点：{}',
        'El end está dentro de la tolerance de varios points: {}',
        'El final está dentro de la tolerancia de varios puntos: {}',
        'La fin est à portée de tolérance de plusieurs points : {}',
        'النهاية ضمن السماحية من عدة نقاط: {}',
    )
    add(
        '两端都空，无法判断方向：{}',
        'Los dos extremos están empty, así que no se puede juzgar la direction: {}',
        'Los dos extremos están vacíos, así que no se puede juzgar la dirección: {}',
        'Les deux extrémités sont vides, donc le sens ne peut pas être jugé : {}',
        'الطرفان فارغان، لذلك لا يمكن حكم الاتجاه: {}',
    )
    add(
        '一端空，无法判断方向：{}',
        'Un extremo está empty, así que no se puede juzgar la direction: {}',
        'Un extremo está vacío, así que no se puede juzgar la dirección: {}',
        'Une extrémité est vide, donc le sens ne peut pas être jugé : {}',
        'طرف واحد فارغ، لذلك لا يمكن حكم الاتجاه: {}',
    )
    add(
        '{} #{} 找不到要素',
        '{} #{} no se encontró el feature',
        '{} #{} no se encontró el elemento',
        '{} #{} entité introuvable',
        '{} #{} لم يُعثر على العنصر',
    )
    add(
        '{} #{} 无法翻转',
        '{} #{} no se puede reverse',
        '{} #{} no se puede invertir',
        '{} #{} ne peut pas être inversé',
        '{} #{} لا يمكن قلبه',
    )
    add(
        '{} #{} 改几何失败',
        '{} #{} falló al cambiar la geometría',
        '{} #{} falló al cambiar la geometría',
        '{} #{} échec du changement de géométrie',
        '{} #{} فشل تغيير الهندسة',
    )
    add(
        '未从光交通到，不判断方向：{}',
        'No se alcanzó desde un cabinet, así que no se juzga la direction: {}',
        'No se alcanzó desde un armario, así que no se juzga la dirección: {}',
        "Non atteint depuis une armoire, donc le sens n'est pas jugé : {}",
        'لم يُبلَغ من كابينة، لذلك لا يُحكم الاتجاه: {}',
    )
    add(
        '<div>… 还有 {} 条</div>',
        '<div>… {} más</div>',
        '<div>… {} más</div>',
        '<div>… {} de plus</div>',
        '<div>… {} أخرى</div>',
    )
    add(
        '起点是起点图层筛选后的全部点，不用挑：有几个点就同时从几个点出发，离线近的先算。线在左，终点在右，都可以加多条并各自筛选分类。终点可以不选。每个线端点是一个连接点：从一个点分出多条线时，每条都顺着往外走，分叉不算错误。终点只在线成环的地方起作用：环在终点处断开，两边的线各自朝终点走；不成环的地方放了终点也不起作用。环上没有终点时，两头碰面的那条线分不出方向，叫伪成环，并写入临时图层。环上有多个终点，或终点落在线的中间而不是接头上，也无法判断该在哪一处断开，这些线同样写入临时图层，不会当成方向正确。',
        'Los starts son todos los points que quedan tras el filter de la start layer; there are no que elegir. El recorrido sale de todos a la vez y gana el start más cercano. Las lines van a la izquierda y los ends a la derecha; puede añadir varias de cada y filter cada una. Los ends son opcionales. Cada extremo de line es un junction: si varias lines salen de un point, se recorre cada una hacia fuera. Las ramas no son errores. Un end solo cuenta donde las lines forman un loop: el loop se corta en el end y ambos lados van hacia él. Donde there are no loop, un end no cambia nada. En un loop sin end, la line donde se encuentran ambos lados no tiene direction; se llama pseudo-loop y se escribe en una layer temporal. Si el loop tiene varios ends, o un end cae en medio de una line y no en un junction, tampoco hay un corte único. Esas lines también van a una layer temporal y no se dan por correct.',
        'Los inicios son todos los puntos que quedan tras el filtro de la capa de inicio; no hay que elegir. El recorrido sale de todos a la vez y gana el inicio más cercano. Las líneas van a la izquierda y los finales a la derecha; puede añadir varias de cada y filtrar cada una. Los finales son opcionales. Cada extremo de línea es un nudo: si varias líneas salen de un punto, se recorre cada una hacia fuera. Las ramas no son errores. Un final solo cuenta donde las líneas forman un bucle: el bucle se corta en el final y ambos lados van hacia él. Donde no hay bucle, un final no cambia nada. En un bucle sin final, la línea donde se encuentran ambos lados no tiene dirección; se llama falso bucle y se escribe en una capa temporal. Si el bucle tiene varios finales, o un final cae en medio de una línea y no en un nudo, tampoco hay un corte único. Esas líneas también van a una capa temporal y no se dan por correctas.',
        "Les départs sont tous les points restant après le filtre de la couche de départ ; rien à choisir. Le parcours part de tous à la fois et le départ le plus proche l'emporte. Les lignes sont à gauche, les fins à droite ; ajoutez-en plusieurs et filtrez chacune. Les fins sont facultatives. Chaque extrémité de ligne est un nœud : si plusieurs lignes partent d'un point, chacune est suivie vers l'extérieur. Les branches ne sont pas des erreurs. Une fin ne compte que là où les lignes forment une boucle : la boucle est coupée à la fin et les deux côtés vont vers elle. Sans boucle, une fin ne change rien. Sur une boucle sans fin, la ligne où les deux côtés se rejoignent n'a pas de sens ; on l'appelle fausse boucle et elle est écrite dans une couche temporaire. Si une boucle a plusieurs fins, ou si une fin tombe au milieu d'une ligne et non sur un nœud, il n'y a pas de coupure unique. Ces lignes sont aussi écrites dans une couche temporaire et ne sont pas tenues pour correctes.",
        'البدايات هي كل النقاط المتبقية بعد تصفية طبقة البداية؛ لا حاجة للاختيار. ينطلق السير منها كلها معًا، والبداية الأقرب هي التي تحدد. الخطوط على اليسار والنهايات على اليمين؛ يمكن إضافة عدة طبقات من كل منهما وتصفية كل واحدة. النهايات اختيارية. كل طرف خط نقطة وصل: إذا خرجت عدة خطوط من نقطة واحدة يُتابع كل منها إلى الخارج. التفرعات ليست أخطاء. النهاية تؤثر فقط حيث تشكّل الخطوط حلقة: تُقطع الحلقة عند النهاية ويتجه الجانبان نحوها. حيث لا توجد حلقة لا تغيّر النهاية شيئًا. على حلقة بلا نهاية، الخط الذي يلتقي عنده الجانبان بلا اتجاه، ويسمى حلقة زائفة ويُكتب في طبقة مؤقتة. إذا كان على الحلقة عدة نهايات، أو وقعت نهاية في منتصف خط لا عند وصلة، فلا موضع قطع واحد. هذه الخطوط تُكتب أيضًا في طبقة مؤقتة ولا تُحسب صحيحة.',
    )
    add(
        '可选。可增加多个终点图层，每条各自筛选分类。终点只在成环、并且能唯一断开时起作用：环上正好一个终点，并且落在线的接头上，环就在那里断开。不成环的地方放了也不起作用。没有唯一断开处时，方向无法判断的线会写入临时图层。',
        'Opcional. Add varias capas de ends y filtre cada una. Un end solo cuenta en un loop cuando es el único corte: exactamente un end, sobre un junction, y el loop se abre ahí. En otros sitios no cambia nada. Si there are no un corte único, las lines sin direction se escriben en una layer temporal.',
        'Opcional. Añada varias capas de finales y filtre cada una. Un final solo cuenta en un bucle cuando es el único corte: exactamente un final, sobre un nudo, y el bucle se abre ahí. En otros sitios no cambia nada. Si no hay un corte único, las líneas sin dirección se escriben en una capa temporal.',
        "Facultatif. Ajoutez plusieurs couches de fins et filtrez chacune. Une fin ne compte sur une boucle que si elle est la coupure unique : exactement une fin, sur un nœud, et la boucle s'ouvre là. Ailleurs elle ne change rien. Sans coupure unique, les lignes sans sens sont écrites dans une couche temporaire.",
        'اختياري. أضف عدة طبقات نهايات وصفِّ كل واحدة. النهاية تؤثر على الحلقة فقط حين تكون القطع الوحيد: نهاية واحدة تمامًا على وصلة، فتُفتح الحلقة هناك. في غير ذلك لا تغيّر شيئًا. إذا لم يوجد قطع واحد، تُكتب الخطوط التي لا يُحسم اتجاهها في طبقة مؤقتة.',
    )
    add(
        '从起点图层的全部点同时往外走，离线近的起点先算。线的两端在容差内才算接到同一个点，缝更大就停下。',
        'Every filtered point on the start layer walks outward at once; nearer starts win. Line ends join only within the tolerance; larger gaps stop the walk.',
        'Se recorre hacia fuera desde todos los puntos de la capa de inicio a la vez; el inicio más cercano cuenta primero. Dos extremos solo son el mismo punto dentro de la tolerancia; una separación mayor detiene el recorrido.',
        "Le parcours part de tous les points de la couche de départ à la fois ; le départ le plus proche compte d'abord. Deux extrémités ne sont un même nœud que dans la tolérance ; un écart plus grand arrête le parcours.",
        'يمشي إلى الخارج من جميع نقاط طبقة البداية دفعة واحدة؛ والأقرب للخط يُحسب أولا. لا تُعد نهايتان نقطة واحدة إلا داخل السماحية؛ والفجوة الأكبر توقف المشي.',
    )
    add(
        '每个线端点是一个连接点：从一个点分出几条线，每条都顺着往外走，分叉不算错误。',
        'Each line endpoint is a junction: when several lines leave one point, each is walked outward; forks are not errors.',
        'Cada extremo de línea es un nudo: si varias líneas salen de un punto, se recorre cada una hacia fuera. Las ramas no son errores.',
        "Chaque extrémité de ligne est un nœud : si plusieurs lignes partent d'un point, chacune est suivie vers l'extérieur. Les branches ne sont pas des erreurs.",
        'كل طرف خط نقطة وصل: إذا خرجت عدة خطوط من نقطة واحدة يُتابع كل منها إلى الخارج. التفرعات ليست أخطاء.',
    )
    add(
        '线走到头断掉是正常现象，不算错误。',
        'A line that stops at a dead end is normal and is not an error.',
        'Que una línea simplemente termine es normal, no un error.',
        "Une ligne qui s'arrête simplement est normal, pas une erreur.",
        'انتهاء الخط عند رأسه أمر طبيعي وليس خطأ.',
    )
    add(
        '请选择点图层。',
        'Choose a point layer.',
        'Elija una capa de puntos.',
        'Choisissez une couche de points.',
        'اختر طبقة نقاط.',
    )
    add(
        '请至少增加一个线图层。',
        'Add at least one line layer.',
        'Añada al menos una capa de líneas.',
        'Ajoutez au moins une couche de lignes.',
        'أضف طبقة خطوط واحدة على الأقل.',
    )
    add(
        '吸附容差必须大于 0。请先在参数配置里设置。',
        'Snap tolerance must be greater than 0. Set it in Parameters first.',
        'La tolerancia de ajuste debe ser mayor que 0. Fíjela arriba antes de empezar.',
        "La tolérance d'accrochage doit être supérieure à 0. Réglez-la au-dessus avant de démarrer.",
        'يجب أن تكون سماحية الالتقاط أكبر من 0. اضبطها في الأعلى قبل البدء.',
    )
    add(
        '正在读取起点',
        'Reading start points',
        'Leyendo el punto de inicio',
        'Lecture du point de départ',
        'قراءة نقطة البداية',
    )
    add(
        '正在连接端点',
        'Connecting endpoints',
        'Conectando extremos',
        'Connexion des extrémités',
        'وصل الأطراف',
    )
    add(
        '正在沿起点往外走',
        'Walking outward from the starts',
        'Recorriendo desde el inicio',
        'Parcours depuis le départ',
        'السير من البداية إلى الخارج',
    )
    add(
        '所选线图层没有错误：每一段都能从起点走到。',
        'No errors on the chosen line layers: every segment is reachable from a start.',
        'Sin errores en las capas de líneas elegidas: cada tramo es alcanzable desde un inicio.',
        'Aucune erreur dans les couches de lignes choisies : chaque tronçon est atteignable depuis un départ.',
        'لا أخطاء في طبقات الخطوط المختارة: كل جزء يمكن بلوغه من بداية.',
    )
    add(
        '从起点走到的线方向都正确。',
        'Every reachable line already points the right way.',
        'Todas las líneas alcanzadas desde el inicio ya apuntan bien.',
        'Toutes les lignes atteintes depuis le départ sont déjà dans le bon sens.',
        'كل الخطوط المبلوغة من البداية تشير الاتجاه الصحيح.',
    )
    add(
        '端点按容差链式合并：A 靠近 B、B 靠近 C 时，三个端点算同一个点，即使 A 和 C 相距超过容差。端点很密的地方要留意。',
        'Endpoints merge by tolerance in a chain: if A is near B and B is near C, all three count as one point even when A and C are farther than the tolerance. Watch dense endpoint clusters.',
        'Los extremos se encadenan por tolerancia: si A está cerca de B y B de C, los tres son un punto, aunque A y C estén más lejos que la tolerancia. Tenga cuidado donde los extremos estén muy juntos.',
        'Les extrémités sont chaînées par la tolérance : si A est près de B et B près de C, les trois sont un seul point, même si A et C sont plus éloignés que la tolérance. Attention là où les extrémités sont denses.',
        'الأطراف تُدمج بالسلسلة حسب السماحية: إذا كان A قريبًا من B وB من C، فالثلاثة نقطة واحدة حتى لو بعد A عن C أكثر من السماحية. انتبه حيث تتكاثف الأطراف.',
    )
    add(
        '吸附容差（米）',
        'Snap tolerance (m)',
        'Tolerancia de ajuste (m)',
        "Tolérance d'accrochage (m)",
        'سماحية الالتقاط (م)',
    )
    add(
        '起点图层',
        'Start layer',
        'Capa de inicio',
        'Couche de départ',
        'طبقة البداية',
    )
    add(
        '按分类筛选。图例未勾选的分类也会列出来，勾上即可参与。',
        'Filter by category. Categories unchecked in the legend are listed too; check them to include them.',
        'Filtrar por categoría. Las categorías apagadas en la leyenda también se listan. Márquelas para incluirlas.',
        'Filtrer par catégorie. Les catégories éteintes dans la légende sont aussi listées. Cochez-les pour les inclure.',
        'تصفية حسب التصنيف. الفئات المطفأة في وسيلة الإيضاح تُسرد أيضًا. علّمها لتُدرج.',
    )
    add(
        '终点',
        'End',
        'Final',
        'Fin',
        'نهاية',
    )
    add(
        '保存当前选择的起点、线和终点图层。只有点这里，下次打开才会恢复这些图层。',
        'Save the current start, line, and end layers. Only this button restores them next time.',
        'Guarda las capas de inicio, línea y final elegidas ahora. La próxima vez se recuperan solo si guarda.',
        'Enregistre les couches de départ, de ligne et de fin choisies maintenant. Elles ne reviendront la prochaine fois que si vous enregistrez.',
        'احفظ طبقات البداية والخط والنهاية المختارة الآن. لا تُستعاد في المرة القادمة إلا إذا حفظت.',
    )
    add(
        '可增加多个线图层。每条线各自按分类筛选。',
        'You can add several line layers. Each one has its own category filter.',
        'Puede añadir varias capas de líneas. Cada una tiene su propio filtro de categoría.',
        'Vous pouvez ajouter plusieurs couches de lignes. Chacune a son propre filtre de catégorie.',
        'يمكن إضافة عدة طبقات خطوط. لكل واحدة تصفية فئات خاصة.',
    )
    add(
        '已保存当前图层。下次打开会恢复这些图层。',
        'Current layers saved. They will be restored next time.',
        'Capas actuales guardadas. Volverán la próxima vez que abra esto.',
        'Couches actuelles enregistrées. Elles reviendront à la prochaine ouverture.',
        'حُفظت الطبقات الحالية. ستعود في المرة القادمة التي تفتح فيها هذه النافذة.',
    )
    add(
        '筛选后的起点图层里没有点。',
        'No points left on the start layer after filtering.',
        'La capa de inicio no tiene puntos tras el filtro.',
        "La couche de départ n'a plus de points après le filtre.",
        'لا توجد نقاط في طبقة البداية بعد الفلترة.',
    )
    add(
        '线图层筛选后没有可用的线。',
        'No usable lines left after filtering the line layers.',
        'Tras el filtro, las capas de líneas no tienen líneas útiles.',
        "Après filtrage, les couches de lignes n'ont pas de lignes utilisables.",
        'بعد التصفية لا توجد خطوط صالحة في طبقات الخطوط.',
    )
    add(
        '容差 {} 米。起点 {} 个（分类筛选后），接上线 {} 个。',
        'Tolerance {} m. Start points {} (after category filter), lines attached {}.',
        'Tolerancia {} m. {} puntos de inicio (tras el filtro de categoría), {} conectados a una línea.',
        'Tolérance {} m. {} points de départ (après le filtre de catégorie), {} raccordés à une ligne.',
        'السماحية {} م. {} نقطة بداية (بعد فلترة الفئات)، و{} متصلة بخط.',
    )
    add(
        '数字化方向反了：{}',
        'Digitized direction is reversed: {}',
        'La dirección digitalizada está invertida: {}',
        'Le sens numérisé est inversé : {}',
        'الاتجاه المرقمن معكوس: {}',
    )
    add(
        '方向反了 {} 条：可修复里默认打勾，用「翻转勾选」。伪成环也在表里，默认不勾。',
        '{} feature(s) reversed: checked by default on Fixable — use “Reverse checked”. Pseudo-loops are listed too, unchecked by default.',
        '{} líneas invertidas empiezan marcadas en Reparable. Use Invertir marcadas. Los falsos bucles también están en la tabla y empiezan sin marcar.',
        '{} lignes inversées commencent cochées dans Réparable. Utilisez Inverser la sélection. Les fausses boucles y figurent aussi et commencent décochées.',
        '{} خطوط معكوسة تبدأ معلَّمة في القابل للإصلاح. استخدم قلب المعلَّم. الحلقات الكاذبة في الجدول أيضًا وتبدأ بلا علامة.',
    )
    add(
        '起点 {} 个（分类筛选后），接上线 {} 个。线 {} 段（要素按段走，多段线各段分开接）。',
        'Start points {} (after category filter), lines attached {}. {} segment(s) (features walked per part; multipart lines connect separately).',
        '{} puntos de inicio (tras el filtro de categoría), {} conectados a una línea. {} tramos de línea (las multipartes conectan por tramo).',
        '{} points de départ (après le filtre de catégorie), {} raccordés à une ligne. {} tronçons de ligne (les multiparties se raccordent par tronçon).',
        '{} نقطة بداية (بعد فلترة الفئات)، و{} متصلة بخط. {} جزء خط (المتعددة الأجزاء تتصل جزءا جزءا).',
    )
    add(
        '走到 {} 段，方向正确 {} 段，方向反了 {} 条要素，伪成环 {} 段。',
        'Reached {} segment(s); correct {} segment(s); reversed {} feature(s); pseudo-loop {} segment(s).',
        'Alcanzados {} tramos: {} correctos, {} elementos invertidos, {} tramos de falso bucle.',
        '{} tronçons atteints : {} dans le bon sens, {} entités inversées, {} tronçons en fausse boucle.',
        'بُلغ {} أجزاء: {} صحيحة، {} عناصر معكوسة، {} أجزاء حلقة كاذبة.',
    )
    add(
        '错误（唯一一类）：未从任何起点走到 {} 段。',
        'Error (only class): {} segment(s) not reached from any start.',
        'Errores (un solo tipo): {} tramos no alcanzados desde ningún inicio.',
        'Erreurs (un seul type) : {} tronçons atteints depuis aucun départ.',
        'أخطاء (نوع واحد فقط): {} جزءا لم يُبلغ من أي بداية.',
    )
    add(
        '分叉会每条都走。断口大于容差 {} 米就停。',
        'Every branch is walked. Stops when a gap is larger than tolerance {} m.',
        'Se recorre cada ramal. Un hueco mayor de {} m detiene el recorrido.',
        'Chaque branche est parcourue. Un écart supérieur à {} m arrête le parcours.',
        'يُسار كل فرع. فجوة أكبر من {} م توقف السير.',
    )
    add(
        '起点{}',
        'Start {}',
        'Inicio {}',
        'Départ {}',
        'البداية {}',
    )
    add(
        ' 段',
        ' part',
        ' tramos',
        ' tronçons',
        ' أجزاء',
    )
    add(
        '开始',
        'Start',
        'Iniciar',
        'Démarrer',
        'بدء',
    )
    add(
        '通用线方向',
        'Free-start line direction',
        'Dirección de líneas',
        'Sens des lignes',
        'اتجاه الخطوط',
    )
    add(
        '请先选择图层。',
        'Choose layers first.',
        'Elija una capa primero.',
        "Choisissez d'abord une couche.",
        'اختر طبقة أولًا.',
    )
    add(
        '请选择点图层，并至少增加一个线图层。',
        'Choose a point layer and add at least one line layer.',
        'Elija una capa de puntos y añada al menos una capa de líneas.',
        'Choisissez une couche de points et ajoutez au moins une couche de lignes.',
        'اختر طبقة نقاط وأضف طبقة خطوط واحدة على الأقل.',
    )
    add(
        '终点 {} 处，其中 {} 处在环上，把环在那里断开；其余不在环上，不起作用。',
        '{} ends; {} están en un loop y lo cortan ahí. Los demás no están en un loop y no cambian nada.',
        '{} finales; {} están en un bucle y lo cortan ahí. Los demás no están en un bucle y no cambian nada.',
        '{} fins ; {} sont sur une boucle et la coupent à cet endroit. Les autres ne sont pas sur une boucle et ne changent rien.',
        '{} نهايات؛ منها {} على حلقة فتقطعها هناك. البقية ليست على حلقة ولا تغيّر شيئًا.',
    )
    add(
        '  自环  {}',
        '  loop propio  {}',
        '  bucle propio  {}',
        '  boucle  {}',
        '  حلقة ذاتية  {}',
    )
    add(
        '方向无法判断：环上有多个终点，或终点不在接头上，无法确定该在哪一处断开。已写入临时图层。',
        'Direction sin decidir: el loop tiene varios ends, o un end no está en un junction, así que there are no un único corte. Escrito en una layer temporal.',
        'Dirección sin decidir: el bucle tiene varios finales, o un final no está en un nudo, así que no hay un único corte. Escrito en una capa temporal.',
        "Sens indécis : la boucle a plusieurs fins, ou une fin n'est pas sur un nœud, donc aucune coupure unique. Écrit dans une couche temporaire.",
        'اتجاه غير محسوم: على الحلقة عدة نهايات، أو النهاية ليست على وصلة، فلا قطع واحد. كُتب في طبقة مؤقتة.',
    )
    add(
        '伪成环：两边不靠这条线也能从起点走到，分不出方向。已写入临时图层。',
        'Pseudo-loop: los dos lados se alcanzan desde el start sin esta line, así que la direction queda abierta. Escrito en una layer temporal.',
        'Falso bucle: los dos lados se alcanzan desde el inicio sin esta línea, así que la dirección queda abierta. Escrito en una capa temporal.',
        'Fausse boucle : les deux côtés sont atteints depuis un départ sans cette ligne, le sens reste ouvert. Écrit dans une couche temporaire.',
        'حلقة زائفة: الطرفان يُبلغان من بداية دون هذا الخط، فيبقى الاتجاه مفتوحًا. كُتب في طبقة مؤقتة.',
    )
    add(
        '方向无法判断：环上有多个终点，或终点不在接头上，无法确定该在哪一处断开。已写入临时图层。默认不勾。',
        'Direction sin decidir: el loop tiene varios ends, o un end no está en un junction, así que there are no un único corte. Escrito en una layer temporal. Desmarcado por defecto.',
        'Dirección sin decidir: el bucle tiene varios finales, o un final no está en un nudo, así que no hay un único corte. Escrito en una capa temporal. Desmarcado por defecto.',
        "Sens indécis : la boucle a plusieurs fins, ou une fin n'est pas sur un nœud, donc aucune coupure unique. Écrit dans une couche temporaire. Décoché par défaut.",
        'اتجاه غير محسوم: على الحلقة عدة نهايات، أو النهاية ليست على وصلة، فلا قطع واحد. كُتب في طبقة مؤقتة. بلا علامة افتراضيًا.',
    )
    add(
        '伪成环：两边不靠这条线也能从起点走到，分不出方向。已写入临时图层。默认不勾，打勾才对调两端。',
        'Pseudo-loop: los dos lados se alcanzan desde el start sin esta line, así que la direction queda abierta. Escrito en una layer temporal. Desmarcado por defecto; márquelo para cambiar los extremos.',
        'Falso bucle: los dos lados se alcanzan desde el inicio sin esta línea, así que la dirección queda abierta. Escrito en una capa temporal. Desmarcado por defecto; márquelo para cambiar los extremos.',
        "Fausse boucle : les deux côtés s'atteignent depuis le départ sans cette ligne, le sens reste ouvert. Écrit dans une couche temporaire. Décoché par défaut ; cochez pour échanger les extrémités.",
        'حلقة زائفة: الجانبان يُبلغان من البداية دون هذا الخط، فيبقى الاتجاه مفتوحًا. كُتب في طبقة مؤقتة. غير معلَّم افتراضيًا؛ علّمه لتبديل الطرفين.',
    )
    add(
        '未走到 {} 段：无法从任何起点到达，这是唯一的错误。',
        '{} segments sin alcanzar: ningún start llega a ellos. Este es el único error.',
        '{} tramos sin alcanzar: ningún inicio llega a ellos. Este es el único error.',
        "{} tronçons non atteints : aucun départ n'y arrive. C'est la seule erreur.",
        '{} جزءا لم يُبلغ: لا تصل إليه أي بداية. هذا هو الخطأ الوحيد.',
    )
    add(
        '伪成环 {} 段：环上没有终点，两头都能走到，分不出方向。已写入临时图层。环上只放一个终点、并且落在线的接头上，再检查一次才能定方向。',
        '{} segments de pseudo-loop: el loop no tiene end, se llega por ambos lados y la direction queda abierta. Escrito en una layer temporal. Ponga exactamente un end en un junction del loop y vuelva a comprobar para fijar la direction.',
        '{} tramos de falso bucle: el bucle no tiene final, se llega por ambos lados y la dirección queda abierta. Escrito en una capa temporal. Ponga exactamente un final en un nudo del bucle y vuelva a comprobar para fijar la dirección.',
        "{} tronçons de fausse boucle : la boucle n'a pas de fin, les deux côtés sont atteints et le sens reste ouvert. Écrit dans une couche temporaire. Placez exactement une fin sur un nœud de la boucle, puis relancez le contrôle pour fixer le sens.",
        '{} أجزاء حلقة زائفة: لا توجد نهاية على الحلقة ويُوصل إلى الطرفين، فيبقى الاتجاه غير محدد. كُتب في طبقة مؤقتة. ضع نهاية واحدة تمامًا على وصلة من الحلقة ثم أعد الفحص لحسم الاتجاه.',
    )
    add(
        '方向无法判断 {} 段：环上的终点不能唯一断开这个环。已写入临时图层，请在地图上查看。',
        '{} segments sin direction: los ends del loop no dan un corte único. Escritos en una layer temporal; mírelos en el mapa.',
        '{} tramos sin dirección: los finales del bucle no dan un corte único. Escritos en una capa temporal; mírelos en el mapa.',
        '{} tronçons au sens indécis : les fins de la boucle ne donnent pas une coupure unique. Écrits dans une couche temporaire ; regardez-les sur la carte.',
        '{} أجزاء بلا اتجاه محسوم: نهايات الحلقة لا تعطي قطعًا واحدًا. كُتبت في طبقة مؤقتة؛ انظرها على الخريطة.',
    )
    add(
        '全部起点在容差 {} 米内都没接到线的端点。缝更大的地方不会跨过去。',
        'Ningún point de start toca un extremo de line dentro de la tolerance {}. Las separaciones mayores no se saltan.',
        'Ningún punto de inicio toca un extremo de línea dentro de la tolerancia {}. Las separaciones mayores no se saltan.',
        'Aucun point de départ ne touche une extrémité de ligne dans la tolérance {}. Les écarts plus grands ne sont pas franchis.',
        'لم تصل أي نقطة بداية إلى نهاية خط داخل سماحية {}. الفجوات الأكبر لا تُعبر.',
    )
    add(
        '  方向无法判断  {}',
        '  Direction sin decidir  {}',
        '  Dirección sin decidir  {}',
        '  Sens indécis  {}',
        '  اتجاه غير محسوم  {}',
    )
    add(
        '  伪成环  {}',
        '  pseudo-loop  {}',
        '  falso bucle  {}',
        '  fausse boucle  {}',
        '  حلقة كاذبة  {}',
    )
    add(
        '  未走到  {}',
        '  no alcanzado  {}',
        '  no alcanzado  {}',
        '  non atteint  {}',
        '  لم يُبلَغ  {}',
    )
    add(
        '  正向  {}',
        '  correct  {}',
        '  correcto  {}',
        '  bon sens  {}',
        '  صحيح  {}',
    )
    add(
        '  各段未全走到或方向不一致，不整条翻转  {}',
        '  segments sin alcanzar todos o direcciones que no coinciden; la line entera no se invierte  {}',
        '  tramos sin alcanzar todos o direcciones que no coinciden; la línea entera no se invierte  {}',
        "  tronçons pas tous atteints ou directions divergentes ; la ligne entière n'est pas inversée  {}",
        '  أجزاء لم تُبلغ كلها أو الاتجاهات متعارضة؛ لا يُقلب الخط كاملا  {}',
    )
    add(
        '起点{} {}',
        'Start {} {}',
        'Inicio {} {}',
        'Départ {} {}',
        'البداية {} {}',
    )
    add(
        '终点{} {}',
        'End {} {}',
        'Final {} {}',
        'Fin {} {}',
        'النهاية {} {}',
    )
    add(
        '{} 段{}',
        '{} segments{}',
        '{} tramos{}',
        '{} tronçons{}',
        '{} أجزاء{}',
    )
    add(
        '未从任何起点走到：{}',
        'No se llega desde ningún start: {}',
        'No se llega desde ningún inicio: {}',
        'Atteint depuis aucun départ : {}',
        'لم يُبلغ من أي بداية: {}',
    )
    add(
        '无法开始',
        'Cannot start',
        'No se puede empezar',
        'Impossible de démarrer',
        'تعذر البدء',
    )
    add(
        '终点{}',
        'End {}',
        'Final {}',
        'Fin {}',
        'نهاية {}',
    )
    add(
        '接头配线另一端不是分纤盒：{}',
        'El otro extremo de la linea de distribucion de este splice no es una FAT box: {}',
        'El otro extremo de la linea de distribucion de este empalme no es una caja FAT: {}',
        "L'autre extremite de la ligne de distribution de cette epissure n'est pas un boitier FAT : {}",
        'الطرف الآخر لخط توزيع هذا المفصل ليس علبة توزيع: {}',
    )
    add(
        '两条下接主干户数相同且到下一接头距离差不到 1 毫米：{} / {}',
        'Dos troncales downstream tienen los mismos households y llegan al siguiente splice a menos de 1 mm: {} / {}',
        'Dos troncales aguas abajo tienen los mismos hogares y llegan al siguiente empalme a menos de 1 mm: {} / {}',
        "Deux troncons aval ont le meme nombre de foyers et atteignent l'epissure suivante a moins de 1 mm : {} / {}",
        'جذعان لاحقان لهما نفس عدد المشتركين ويصلان إلى المفصل التالي بفارق أقل من 1 مم: {} / {}',
    )
    add(
        '配线成环：{}',
        'Bucle de distribucion: {}',
        'Bucle de distribucion: {}',
        'Boucle de distribution : {}',
        'حلقة توزيع: {}',
    )
    add(
        '分纤盒分叉（出 {} 条配线）：{}',
        'Ramal de FAT box ({} lineas de distribucion): {}',
        'Ramal de caja FAT ({} lineas de distribucion): {}',
        'Branchement de boitier FAT ({} lignes de distribution) : {}',
        'تفرع علبة التوزيع ({} خطوط توزيع خارجة): {}',
    )
    add(
        '两条链路户数相同且到首盒距离差不到 1 毫米：{} / {}',
        'Dos rutas tienen los mismos households y llegan a la primera caja a menos de 1 mm: {} / {}',
        'Dos rutas tienen los mismos hogares y llegan a la primera caja a menos de 1 mm: {} / {}',
        'Deux liaisons ont le meme nombre de foyers et atteignent le premier boitier a moins de 1 mm : {} / {}',
        'مساران لهما نفس عدد المشتركين ويصلان إلى أول علبة بفارق أقل من 1 مم: {} / {}',
    )
    add(
        '配线两端接到同一接头：{}',
        'Los dos extremos de la linea de distribucion llegan al mismo splice: {}',
        'Los dos extremos de la linea de distribucion llegan al mismo empalme: {}',
        'Les deux extremites de la ligne de distribution aboutissent a la meme epissure : {}',
        'طرفا خط التوزيع يصلان إلى المفصل نفسه: {}',
    )
    add(
        '接头后面没有配线，没有分纤盒可命名：{}',
        'De este splice no sale ninguna linea de distribucion, there are no FAT box que nombrar: {}',
        'De este empalme no sale ninguna linea de distribucion, no hay caja FAT que nombrar: {}',
        'Aucune ligne de distribution ne sort de cette epissure, aucun boitier FAT a nommer : {}',
        'لا يخرج خط توزيع من هذا المفصل، فلا توجد علبة توزيع لتسميتها: {}',
    )
    add(
        '分纤盒被多条配线占用：{}',
        'FAT box alcanzada por mas de una linea de distribucion: {}',
        'Caja FAT alcanzada por mas de una linea de distribucion: {}',
        "Boitier FAT atteint par plus d'une ligne de distribution : {}",
        'علبة التوزيع تصلها أكثر من خط توزيع: {}',
    )
    add(
        '一端空',
        'Un extremo abierto',
        'Un extremo abierto',
        'Une extrémité ouverte',
        'طرف واحد فارغ',
    )
    add(
        '两端都是分纤盒',
        'Los dos extremos son FAT boxes',
        'Los dos extremos son cajas FAT',
        'Les deux extremites sont des boitiers FAT',
        'الطرفان علبتا توزيع',
    )
    add(
        '两端都是用户',
        'Los dos extremos son usuarios',
        'Los dos extremos son usuarios',
        'Les deux extremites sont des abonnes',
        'الطرفان مستخدمان',
    )
    add(
        '{}接到{}',
        '{} unido a {}',
        '{} unido a {}',
        '{} relie a {}',
        '{} متصل بـ {}',
    )
    add(
        '光缆{}同时靠近多个点：{}',
        'El cable {} esta cerca de varios points: {}',
        'El cable {} esta cerca de varios puntos: {}',
        'Le cable {} est proche de plusieurs points : {}',
        'الكبل {} قريب من عدة نقاط: {}',
    )
    add(
        '第四段：光交出线按第一段主干短的号小，一样长再比角度。第一个接头 01-01。没分叉第五段一直 01，第六段按走过的顺序。分叉时户数多的接着当前第五段，少的新开第五段，第六段接最大号后面。',
        'Segment 4: las salidas del cabinet reciben un número menor si el primer segment de feeder es más corto; si miden igual, se usa el ángulo. El primer splice es 01-01. Sin ramal, el segment 5 sigue en 01 y el segment 6 sigue el orden del recorrido. En un ramal, el lado con más households conserva el segment 5 actual, el menor abre un segment 5 nuevo, y el segment 6 continúa después del número más alto.',
        'Tramo 4: las salidas del armario reciben un número menor si el primer tramo de alimentador es más corto; si miden igual, se usa el ángulo. El primer empalme es 01-01. Sin ramal, el tramo 5 sigue en 01 y el tramo 6 sigue el orden del recorrido. En un ramal, el lado con más hogares conserva el tramo 5 actual, el menor abre un tramo 5 nuevo, y el tramo 6 continúa después del número más alto.',
        "Tronçon 4 : les sorties d'armoire reçoivent un plus petit numéro si le premier tronçon d'alimentation est plus court ; à longueur égale, l'angle départage. La première épissure est 01-01. Sans branche, le tronçon 5 reste 01 et le tronçon 6 suit l'ordre du parcours. À une branche, le côté avec plus de foyers garde le tronçon 5 actuel, le plus petit ouvre un nouveau tronçon 5, et le tronçon 6 continue après le plus grand numéro.",
        'الجزء الرابع: مخارج الكابينة تأخذ رقمًا أصغر إذا كان أول جزء تغذية أقصر؛ وعند تساوي الطول يُستخدم الزاوية. أول وصلة 01-01. بلا تفرع يبقى الجزء الخامس 01 ويتبع السادس ترتيب السير. عند التفرع، الجانب ذو الأسر الأكثر يبقي الجزء الخامس الحالي، والأقل يفتح جزءًا خامسًا جديدًا، والسادس يتابع بعد أكبر رقم.',
    )
    add(
        '同一 ODF 的配线放在一起排。第五段从该 ODF 接头第五段最大值 +1 起，户数多的号小，相同则到首盒线长更长的号小。每条链第六段从 01 起，离接头近的是 01。不跟接头共用第五段。',
        'Los cables de distribution del mismo ODF se numeran juntos. El segment 5 empieza en el mayor segment 5 de ese splice ODF más 1. Más households reciben el número menor; si empatan, la line más larga hasta la primera FAT box recibe el menor. El segment 6 de cada cadena empieza en 01, y el trozo más cercano al splice es 01. No comparte el segment 5 con el splice.',
        'Los cables de distribución del mismo ODF se numeran juntos. El tramo 5 empieza en el mayor tramo 5 de ese empalme ODF más 1. Más hogares reciben el número menor; si empatan, la línea más larga hasta la primera caja FAT recibe el menor. El tramo 6 de cada cadena empieza en 01, y el trozo más cercano al empalme es 01. No comparte el tramo 5 con el empalme.',
        "Les câbles de distribution d'un même ODF sont numérotés ensemble. Le tronçon 5 commence au plus grand tronçon 5 de cette épissure ODF plus 1. Plus de foyers reçoivent le plus petit numéro ; à égalité, la ligne plus longue jusqu'au premier FAT reçoit le plus petit. Le tronçon 6 de chaque chaîne commence à 01, et le morceau le plus près de l'épissure est 01. Il ne partage pas le tronçon 5 avec l'épissure.",
        'كبلات التوزيع لنفس ODF تُرقَّم معًا. الجزء الخامس يبدأ من أكبر جزء خامس لوصلة ODF تلك زائد 1. الأسر الأكثر تأخذ الرقم الأصغر؛ وعند التساوي، الخط الأطول إلى أول علبة يأخذ الأصغر. الجزء السادس لكل سلسلة يبدأ من 01، والقطعة الأقرب إلى الوصلة هي 01. لا يشارك الجزء الخامس مع الوصلة.',
    )
    add(
        '看懂当前选项',
        'Entender la opción actual',
        'Entender la opción actual',
        'Comprendre le choix actuel',
        'فهم الخيار الحالي',
    )
    add(
        '模拟预览（固定示意网，不读图层）',
        'Vista de ejemplo (una red fija, no lee capas)',
        'Vista de ejemplo (una red fija, no lee capas)',
        "Aperçu d'exemple (un réseau fixe, sans lire les couches)",
        'معاينة مثال (شبكة ثابتة، لا تقرأ الطبقات)',
    )
    add(
        '实际测试（读当前图层，不写入）',
        'Prueba real (lee las capas actuales, no escribe)',
        'Prueba real (lee las capas actuales, no escribe)',
        "Test réel (lit les couches actuelles, n'écrit rien)",
        'اختبار فعلي (يقرأ الطبقات الحالية ولا يكتب)',
    )
    add(
        '最多 ',
        'Máx. ',
        'Máx. ',
        'Max. ',
        'حتى ',
    )
    add(
        ' 条',
        ' filas',
        ' filas',
        ' lignes',
        ' صفوف',
    )
    add(
        '运行测试',
        'Ejecutar prueba',
        'Ejecutar prueba',
        'Lancer le test',
        'تشغيل الاختبار',
    )
    add(
        '按左边当前方案和上面选的功能，对图层跑一遍分析。只出表，不写字段、不出临时图层。',
        'Ejecuta la herramienta elegida con el scheme actual. Solo llena la tabla. No escribe campos ni crea capas.',
        'Ejecuta la herramienta elegida con el esquema actual. Solo llena la tabla. No escribe campos ni crea capas.',
        "Lance l'outil choisi avec le schéma actuel. Il ne remplit que le tableau. Il n'écrit pas de champs et ne crée pas de couches.",
        'يشغّل الأداة المختارة بالمخطط الحالي. يملأ الجدول فقط. لا يكتب حقولًا ولا ينشئ طبقات.',
    )
    add(
        '用本窗里还没确定的容差、角度、六个方案做全面检测。只出表，不写字段、不翻线、不出图层。',
        'Hace la comprobación completa con la tolerance, el ángulo y los seis esquemas de esta ventana, aunque no los haya confirmado. Solo tabla: no escribe, no invierte lines, no crea capas.',
        'Hace la comprobación completa con la tolerancia, el ángulo y los seis esquemas de esta ventana, aunque no los haya confirmado. Solo tabla: no escribe, no invierte líneas, no crea capas.',
        "Fait le contrôle complet avec la tolérance, l'angle et les six schémas de cette fenêtre, même sans confirmation. Tableau seulement : pas d'écriture, pas d'inversion, pas de couches.",
        'يجري الفحص الكامل بسماحية وزاوية والمخططات الستة في هذه النافذة حتى قبل التأكيد. الجدول فقط: بلا كتابة ولا قلب خطوط ولا طبقات.',
    )
    add(
        '换下拉会立刻改模拟预览。测试和全面检测用本窗当前参数，点取消不会保存。',
        'Cambiar la lista actualiza al momento la vista de ejemplo. La prueba y la comprobación completa usan los ajustes actuales de esta ventana. Cancel no los guarda.',
        'Cambiar la lista actualiza al momento la vista de ejemplo. La prueba y la comprobación completa usan los ajustes actuales de esta ventana. Cancelar no los guarda.',
        "Changer la liste met à jour tout de suite l'aperçu. Le test et le contrôle complet utilisent les réglages actuels de cette fenêtre. Annuler ne les enregistre pas.",
        'تغيير القائمة يحدّث معاينة المثال فورًا. الاختبار والفحص الكامل يستخدمان إعداد هذه النافذة. الإلغاء لا يحفظه.',
    )
    add(
        '没有主窗口，跑不了实际测试。',
        'There are no ventana principal, así que la prueba real no puede ejecutarse.',
        'No hay ventana principal, así que la prueba real no puede ejecutarse.',
        "Il n'y a pas de fenêtre principale, donc le test réel ne peut pas démarrer.",
        'لا توجد نافذة رئيسية، لذلك لا يمكن تشغيل الاختبار الفعلي.',
    )
    add(
        '没有主窗口，跑不了全面检测。',
        'There are no ventana principal, así que la comprobación completa no puede ejecutarse.',
        'No hay ventana principal, así que la comprobación completa no puede ejecutarse.',
        "Il n'y a pas de fenêtre principale, donc le contrôle complet ne peut pas démarrer.",
        'لا توجد نافذة رئيسية، لذلك لا يمكن تشغيل الفحص الكامل.',
    )
    add(
        '先按图层 ID 找（同名图层不会串），找不到再按名称。',
        '先按图层 ID 找（同名图层不会串），找不到再按名称。',
        '先按图层 ID 找（同名图层不会串），找不到再按名称。',
        '先按图层 ID 找（同名图层不会串），找不到再按名称。',
        '先按图层 ID 找（同名图层不会串），找不到再按名称。',
    )
    add(
        '全面检测。只读图层配置，不改赋值和命名的写入规则。',
        '全面检测。只读图层配置，不改赋值和命名的写入规则。',
        '全面检测。只读图层配置，不改赋值和命名的写入规则。',
        '全面检测。只读图层配置，不改赋值和命名的写入规则。',
        '全面检测。只读图层配置，不改赋值和命名的写入规则。',
    )
    add(
        '设备点相距不到容差；线端点容差内有多个点但已按最近接上（歧义的不在这里重复报）。',
        '设备点相距不到容差；线端点容差内有多个点但已按最近接上（歧义的不在这里重复报）。',
        '设备点相距不到容差；线端点容差内有多个点但已按最近接上（歧义的不在这里重复报）。',
        '设备点相距不到容差；线端点容差内有多个点但已按最近接上（歧义的不在这里重复报）。',
        '设备点相距不到容差；线端点容差内有多个点但已按最近接上（歧义的不在这里重复报）。',
    )
    add(
        '端点分不清：容差内同时靠近多个点，或一根线两头吸到同一个点',
        'Extremos ambiguos: hay varios puntos dentro de la tolerancia, o los dos extremos de una línea se ajustan al mismo punto',
        'Extremos ambiguos: hay varios puntos dentro de la tolerancia, o los dos extremos de una línea se ajustan al mismo punto',
        "Extrémités ambiguës : plusieurs points sont dans la tolérance, ou les deux extrémités d'une ligne s'accrochent au même point",
        'أطراف ملتبسة: عدة نقاط داخل السماحية، أو طرفا خط يلتقطان النقطة نفسها',
    )
    add(
        '光缆一端空，或两头角色不对（光交只能对接头，接头可接接头或分纤盒）。两端都空单独算软错误',
        'Un extremo del cable está vacío, o los dos papeles no cuadran (el armario solo se une a un empalme; el empalme puede unirse a un empalme o a una caja FAT). Los dos extremos vacíos son un error leve aparte',
        'Un extremo del cable está vacío, o los dos papeles no cuadran (el armario solo se une a un empalme; el empalme puede unirse a un empalme o a una caja FAT). Los dos extremos vacíos son un error leve aparte',
        "Une extrémité de câble est vide, ou les deux rôles sont faux (une armoire ne rejoint qu'une épissure ; une épissure peut rejoindre une épissure ou un FAT). Les deux extrémités vides sont une erreur souple à part",
        'طرف كابل فارغ، أو الدوران غير صحيحين (الكابينة تلتقي وصلة فقط؛ الوصلة قد تلتقي وصلة أو علبة توزيع). الطرفان الفارغان خطأ مرن منفصل',
    )
    add(
        '光交没有往外的光缆，或有光缆把光交当成下游',
        'El armario no tiene cable de salida, o un cable trata el armario como aguas abajo',
        'El armario no tiene cable de salida, o un cable trata el armario como aguas abajo',
        "L'armoire n'a pas de câble sortant, ou un câble traite l'armoire comme aval",
        'الكابينة بلا كابل خارج، أو كابل يعامل الكابينة كمصب',
    )
    add(
        '接头从光交方向进来的光缆不是恰好 1 条（0 条或多于 1 条）。出去几条不限',
        'El empalme no tiene exactamente un cable que llega desde el armario (cero o más de uno). Las salidas no tienen límite',
        'El empalme no tiene exactamente un cable que llega desde el armario (cero o más de uno). Las salidas no tienen límite',
        "L'épissure n'a pas exactement un câble venant du côté armoire (zéro ou plus d'un). Les sorties ne sont pas limitées",
        'الوصلة ليس فيها كابل واحد بالضبط قادم من جهة الكابينة (صفر أو أكثر من واحد). الكبلات الخارجة بلا حد',
    )
    add(
        '分纤盒从光交方向进来的光缆不是恰好 1 条，或出去超过 1 条。不出去是允许的，分纤盒可以再串分纤盒',
        'La caja FAT no tiene exactamente un cable de entrada desde el armario, o tiene más de un cable de salida. No tener salida está permitido, y una caja puede enlazar con otra',
        'La caja FAT no tiene exactamente un cable de entrada desde el armario, o tiene más de un cable de salida. No tener salida está permitido, y una caja puede enlazar con otra',
        "Le FAT n'a pas exactement un câble entrant du côté armoire, ou il a plus d'un câble sortant. Ne rien faire sortir est permis, et un FAT peut s'enchaîner à un autre",
        'علبة التوزيع ليس فيها كابل داخل واحد بالضبط من جهة الكابينة، أو لها أكثر من كابل خارج. عدم الخروج مسموح، والعلبة قد تتصل بعلبة أخرى',
    )
    add(
        '从光交往外走时绕回去，网络成环',
        'El recorrido desde el armario vuelve sobre sí mismo, así que la red tiene un bucle',
        'El recorrido desde el armario vuelve sobre sí mismo, así que la red tiene un bucle',
        "Le parcours depuis l'armoire revient sur lui-même, donc le réseau a une boucle",
        'السير من الكابينة يعود على نفسه، لذلك الشبكة فيها حلقة',
    )
    add(
        '光缆两头角色是对的，但这根线从任何一个光交都走不到',
        'Los dos papeles del cable son válidos, pero ningún armario alcanza esta línea',
        'Los dos papeles del cable son válidos, pero ningún armario alcanza esta línea',
        "Les deux rôles du câble sont valides, mais aucune armoire n'atteint cette ligne",
        'دورا الكابل صحيحان، لكن لا كابينة تبلغ هذا الخط',
    )
    add(
        '皮线两头必须是分纤盒和用户点。一端空、两头都是盒或都是用户、接到光交或接头。两端都空单独算软错误',
        'La acometida debe unir una caja FAT y un punto de usuario. Un extremo vacío, los dos en caja, los dos en usuario, o un enlace al armario o al empalme, no vale. Los dos extremos vacíos son un error leve aparte',
        'La acometida debe unir una caja FAT y un punto de usuario. Un extremo vacío, los dos en caja, los dos en usuario, o un enlace al armario o al empalme, no vale. Los dos extremos vacíos son un error leve aparte',
        "Le branchement doit relier un FAT et un point usager. Une extrémité vide, les deux sur un FAT, les deux sur un usager, ou un lien vers l'armoire ou l'épissure, est faux. Les deux extrémités vides sont une erreur souple à part",
        'كبل الإسقاط يجب أن يصل علبة توزيع بنقطة مستخدم. طرف فارغ، أو الطرفان علب، أو الطرفان مستخدم، أو وصل إلى كابينة أو وصلة، غير صحيح. الطرفان الفارغان خطأ مرن منفصل',
    )
    add(
        '同一个分纤盒到同一个用户点只允许 1 条皮线。一个分纤盒接不同用户点允许',
        'Solo se permite una acometida de la misma caja FAT al mismo punto de usuario. Una caja puede servir a puntos distintos',
        'Solo se permite una acometida de la misma caja FAT al mismo punto de usuario. Una caja puede servir a puntos distintos',
        'Un seul branchement est permis du même FAT vers le même point usager. Un FAT peut desservir des points différents',
        'يُسمح بكبل إسقاط واحد فقط من علبة التوزيع نفسها إلى نقطة المستخدم نفسها. العلبة قد تخدم نقاطًا مختلفة',
    )
    add(
        '用户点至少要有 1 条合格皮线接到分纤盒',
        'Un punto de usuario necesita al menos una acometida válida hasta una caja FAT',
        'Un punto de usuario necesita al menos una acometida válida hasta una caja FAT',
        'Un point usager doit avoir au moins un branchement valide vers un FAT',
        'نقطة المستخدم تحتاج كبل إسقاط صالحًا واحدًا على الأقل إلى علبة توزيع',
    )
    add(
        '线已经能从光交走到下游，但数字化起点不在上游。可在结果窗里翻转',
        'La línea se alcanza aguas abajo desde el armario, pero el inicio digitalizado no está aguas arriba. Puede invertirla en la ventana de resultados',
        'La línea se alcanza aguas abajo desde el armario, pero el inicio digitalizado no está aguas arriba. Puede invertirla en la ventana de resultados',
        "La ligne est atteinte en aval depuis l'armoire, mais le départ numérisé n'est pas en amont. Vous pouvez l'inverser dans la fenêtre de résultat",
        'يمكن بلوغ الخط في المصب من الكابينة، لكن البداية المرقمنة ليست في المنبع. يمكن قلبه في نافذة النتيجة',
    )
    add(
        '光交/接头/分纤盒之间相距不到吸附容差；线端点容差内有多个点（已按最近的接上，请人工复核）',
        'Un armario, empalme o caja FAT está más cerca que la tolerancia, o un extremo tiene varios puntos dentro de la tolerancia (se usó el más cercano; revíselo)',
        'Un armario, empalme o caja FAT está más cerca que la tolerancia, o un extremo tiene varios puntos dentro de la tolerancia (se usó el más cercano; revíselo)',
        'Une armoire, une épissure ou un FAT est plus proche que la tolérance, ou une extrémité a plusieurs points dans la tolérance (le plus proche a été pris ; à vérifier)',
        'كابينة أو وصلة أو علبة توزيع أقرب من السماحية، أو طرف خط فيه عدة نقاط داخل السماحية (استُخدمت الأقرب؛ راجعها)',
    )
    add(
        '接头、分纤盒、光缆的 CODE 字段有重复值或空值（命名前可不勾）',
        'El campo CODE de un empalme, una caja FAT o un cable está repetido o vacío (puede dejarlo sin marcar antes de nombrar)',
        'El campo CODE de un empalme, una caja FAT o un cable está repetido o vacío (puede dejarlo sin marcar antes de nombrar)',
        "Le champ CODE d'une épissure, d'un FAT ou d'un câble est en double ou vide (vous pouvez le laisser décoché avant de nommer)",
        'حقل CODE لوصلة أو علبة توزيع أو كابل مكرر أو فارغ (يمكن تركه بلا علامة قبل التسمية)',
    )
    add(
        '同一个用户点接到 2 个及以上分纤盒。允许，但请确认。出图层',
        'El mismo punto de usuario se conecta a dos o más cajas FAT. Está permitido; confírmelo. Se crea una capa',
        'El mismo punto de usuario se conecta a dos o más cajas FAT. Está permitido; confírmelo. Se crea una capa',
        "Le même point usager rejoint deux FAT ou plus. C'est permis ; confirmez. Une couche est créée",
        'نقطة المستخدم نفسها تتصل بعلبتين أو أكثر. هذا مسموح؛ يُرجى التأكيد. تُنشأ طبقة',
    )
    add(
        '分纤盒没有接到用户的合格皮线（后面赋户数会是 0）',
        'La caja FAT no tiene una acometida válida hasta un usuario (el relleno de hogares será 0)',
        'La caja FAT no tiene una acometida válida hasta un usuario (el relleno de hogares será 0)',
        "Le FAT n'a pas de branchement valide vers un usager (le remplissage des foyers sera 0)",
        'علبة التوزيع بلا كبل إسقاط صالح إلى مستخدم (ملء الأسر سيكون 0)',
    )
    add(
        '接头后面没有配线（这一支没有分纤盒）',
        'El empalme no tiene cable de distribución después (esta rama no tiene caja FAT)',
        'El empalme no tiene cable de distribución después (esta rama no tiene caja FAT)',
        "L'épissure n'a pas de câble de distribution ensuite (cette branche n'a pas de FAT)",
        'الوصلة بلا كابل توزيع بعدها (هذا الفرع بلا علبة توزيع)',
    )
    add(
        '起点',
        'Start',
        'Inicio',
        'Départ',
        'بداية',
    )
    add(
        '容差 {} 米，{}，起始角 {}°。',
        '容差 {} 米，{}，起始角 {}°。',
        '容差 {} 米，{}，起始角 {}°。',
        '容差 {} 米，{}，起始角 {}°。',
        '容差 {} 米，{}，起始角 {}°。',
    )
    add(
        '正在检查线方向',
        '正在检查线方向',
        '正在检查线方向',
        '正在检查线方向',
        '正在检查线方向',
    )
    add(
        '。当前赋值·皮线方案不会写这些皮线',
        '。当前赋值·皮线方案不会写这些皮线',
        '。当前赋值·皮线方案不会写这些皮线',
        '。当前赋值·皮线方案不会写这些皮线',
        '。当前赋值·皮线方案不会写这些皮线',
    )
    add(
        '{} CODE 重复 {}（{} 个）：{}',
        '{} CODE 重复 {}（{} 个）：{}',
        '{} CODE 重复 {}（{} 个）：{}',
        '{} CODE 重复 {}（{} 个）：{}',
        '{} CODE 重复 {}（{} 个）：{}',
    )
    add(
        '{}同时靠近多个点：{}',
        '{}同时靠近多个点：{}',
        '{}同时靠近多个点：{}',
        '{}同时靠近多个点：{}',
        '{}同时靠近多个点：{}',
    )
    add(
        '{} CODE 字段没配，跳过 CODE 检查。',
        '{} CODE 字段没配，跳过 CODE 检查。',
        '{} CODE 字段没配，跳过 CODE 检查。',
        '{} CODE 字段没配，跳过 CODE 检查。',
        '{} CODE 字段没配，跳过 CODE 检查。',
    )
    add(
        '两个设备点相距不到容差 {} 米：{} / {}',
        '两个设备点相距不到容差 {} 米：{} / {}',
        '两个设备点相距不到容差 {} 米：{} / {}',
        '两个设备点相距不到容差 {} 米：{} / {}',
        '两个设备点相距不到容差 {} 米：{} / {}',
    )
    add(
        '{}容差内有 {} 个点，已接最近的 {}，请复核：{}',
        '{}容差内有 {} 个点，已接最近的 {}，请复核：{}',
        '{}容差内有 {} 个点，已接最近的 {}，请复核：{}',
        '{}容差内有 {} 个点，已接最近的 {}，请复核：{}',
        '{}容差内有 {} 个点，已接最近的 {}，请复核：{}',
    )
    add(
        '{} CODE 为空：{}',
        '{} CODE 为空：{}',
        '{} CODE 为空：{}',
        '{} CODE 为空：{}',
        '{} CODE 为空：{}',
    )
    add(
        '未从光交通到：{}',
        '未从光交通到：{}',
        '未从光交通到：{}',
        '未从光交通到：{}',
        '未从光交通到：{}',
    )
    add(
        '接头后面没有配线：{}',
        '接头后面没有配线：{}',
        '接头后面没有配线：{}',
        '接头后面没有配线：{}',
        '接头后面没有配线：{}',
    )
    add(
        '同一分纤盒到同一用户有 {} 条皮线，只允许 1 条：{} ← {}',
        '同一分纤盒到同一用户有 {} 条皮线，只允许 1 条：{} ← {}',
        '同一分纤盒到同一用户有 {} 条皮线，只允许 1 条：{} ← {}',
        '同一分纤盒到同一用户有 {} 条皮线，只允许 1 条：{} ← {}',
        '同一分纤盒到同一用户有 {} 条皮线，只允许 1 条：{} ← {}',
    )
    add(
        '用户点没有合格皮线：{}',
        '用户点没有合格皮线：{}',
        '用户点没有合格皮线：{}',
        '用户点没有合格皮线：{}',
        '用户点没有合格皮线：{}',
    )
    add(
        '用户接到 {} 个分纤盒：{}（{}）{}',
        '用户接到 {} 个分纤盒：{}（{}）{}',
        '用户接到 {} 个分纤盒：{}（{}）{}',
        '用户接到 {} 个分纤盒：{}（{}）{}',
        '用户接到 {} 个分纤盒：{}（{}）{}',
    )
    add(
        '分纤盒没有合格皮线：{}',
        '分纤盒没有合格皮线：{}',
        '分纤盒没有合格皮线：{}',
        '分纤盒没有合格皮线：{}',
        '分纤盒没有合格皮线：{}',
    )
    add(
        '用户点总户数 {} 与皮线字段总户数 {} 不一致。当前赋值·分纤盒方案核对总户数，赋值时整批不写。',
        '用户点总户数 {} 与皮线字段总户数 {} 不一致。当前赋值·分纤盒方案核对总户数，赋值时整批不写。',
        '用户点总户数 {} 与皮线字段总户数 {} 不一致。当前赋值·分纤盒方案核对总户数，赋值时整批不写。',
        '用户点总户数 {} 与皮线字段总户数 {} 不一致。当前赋值·分纤盒方案核对总户数，赋值时整批不写。',
        '用户点总户数 {} 与皮线字段总户数 {} 不一致。当前赋值·分纤盒方案核对总户数，赋值时整批不写。',
    )
    add(
        '接头没有从光交方向来的进线：{}',
        '接头没有从光交方向来的进线：{}',
        '接头没有从光交方向来的进线：{}',
        '接头没有从光交方向来的进线：{}',
        '接头没有从光交方向来的进线：{}',
    )
    add(
        '分纤盒没有从光交方向来的光缆：{}',
        '分纤盒没有从光交方向来的光缆：{}',
        '分纤盒没有从光交方向来的光缆：{}',
        '分纤盒没有从光交方向来的光缆：{}',
        '分纤盒没有从光交方向来的光缆：{}',
    )
    add(
        '旧公式，当前命名不调用。分纤盒第六段见 format_ranked_fat_code，一律从 01 起。',
        '旧公式，当前命名不调用。分纤盒第六段见 format_ranked_fat_code，一律从 01 起。',
        '旧公式，当前命名不调用。分纤盒第六段见 format_ranked_fat_code，一律从 01 起。',
        '旧公式，当前命名不调用。分纤盒第六段见 format_ranked_fat_code，一律从 01 起。',
        '旧公式，当前命名不调用。分纤盒第六段见 format_ranked_fat_code，一律从 01 起。',
    )
    add(
        '拓扑检查结果',
        'Topology check results',
        'Resultados de topología',
        'Résultats du contrôle topologique',
        'نتائج فحص الطوبولوجيا',
    )
    add(
        '编号',
        '编号',
        '编号',
        '编号',
        '编号',
    )
    add(
        '编码',
        '编码',
        '编码',
        '编码',
        '编码',
    )
    add(
        '设备名称',
        '设备名称',
        '设备名称',
        '设备名称',
        '设备名称',
    )
    add(
        '设备编号',
        '设备编号',
        '设备编号',
        '设备编号',
        '设备编号',
    )
    add(
        '主干',
        'Feeder',
        'Alimentación',
        'Artère',
        'رئيسي',
    )
    add(
        '配线',
        'Distribution',
        'Distribución',
        'Distribution',
        'توزيع',
    )
    add(
        '皮线赋值',
        'Relleno de acometida',
        'Relleno de acometida',
        'Remplissage du branchement',
        'تعبئة كبل الإسقاط',
    )
    add(
        '分纤盒赋值',
        'Relleno de caja FAT',
        'Relleno de caja FAT',
        'Remplissage du boîtier FAT',
        'تعبئة علبة التوزيع',
    )
    add(
        '线赋值',
        'Relleno de cable',
        'Relleno de cable',
        'Remplissage du câble',
        'تعبئة الكابل',
    )
    add(
        '接头 CODE',
        'CODE de empalme',
        'CODE de empalme',
        "CODE d'épissure",
        'رمز الوصلة',
    )
    add(
        '分纤盒 CODE',
        'CODE de caja FAT',
        'CODE de caja FAT',
        'CODE du boîtier FAT',
        'رمز علبة التوزيع',
    )
    add(
        '主干配线CODE',
        'CODE de alimentación y distribución',
        'CODE de alimentación y distribución',
        'CODE artère et distribution',
        'رمز الرئيسي والتوزيع',
    )
    add(
        '线方向',
        'Direction de line',
        'Dirección de línea',
        'Sens de ligne',
        'اتجاه الخط',
    )
    add(
        '同分纤盒重复皮线',
        'Acometidas repetidas en una caja FAT',
        'Acometidas repetidas en una caja FAT',
        'Branchements en double sur un boîtier FAT',
        'كبلات إسقاط مكررة على علبة واحدة',
    )
    add(
        '多分纤盒覆盖用户',
        'Usuario cubierto por varias cajas FAT',
        'Usuario cubierto por varias cajas FAT',
        'Usager couvert par plusieurs boîtiers FAT',
        'مستخدم تغطيه عدة علب',
    )
    add(
        '分纤盒无皮线',
        'Caja FAT sin acometida',
        'Caja FAT sin acometida',
        'Boîtier FAT sans branchement',
        'علبة توزيع بلا كبل إسقاط',
    )
    add(
        '两端空',
        'Ambos extremos abiertos',
        'Ambos extremos abiertos',
        'Les deux extrémités ouvertes',
        'الطرفان فارغان',
    )
    add(
        '皮线两端分纤盒',
        'Acometida entre dos cajas FAT',
        'Acometida entre dos cajas FAT',
        'Branchement entre deux boîtiers FAT',
        'كبل إسقاط بين علبتين',
    )
    add(
        '皮线两端用户',
        'Acometida entre dos usuarios',
        'Acometida entre dos usuarios',
        'Branchement entre deux usagers',
        'كبل إسقاط بين مستخدمين',
    )
    add(
        '端点歧义',
        'Extremo ambiguo',
        'Extremo ambiguo',
        'Extrémité ambiguë',
        'طرف ملتبس',
    )
    add(
        '成环',
        'Bucle',
        'Bucle',
        'Boucle',
        'حلقة',
    )
    add(
        '分纤盒分叉',
        'Ramal en caja FAT',
        'Ramal en caja FAT',
        'Branchement au boîtier FAT',
        'تفرع عند العلبة',
    )
    add(
        '分纤盒多进线',
        'Caja FAT con varias entradas',
        'Caja FAT con varias entradas',
        'Boîtier FAT à plusieurs entrées',
        'علبة بعدة خطوط داخلة',
    )
    add(
        '接头多进线',
        'Empalme con varias entradas',
        'Empalme con varias entradas',
        'Épissure à plusieurs entrées',
        'وصلة بعدة خطوط داخلة',
    )
    add(
        '接头主干分叉',
        'Ramal de alimentación en el empalme',
        'Ramal de alimentación en el empalme',
        "Branchement d'artère à l'épissure",
        'تفرع الرئيسي عند الوصلة',
    )
    add(
        '光交被当作下游',
        'Armario tratado como aguas abajo',
        'Armario tratado como aguas abajo',
        'Armoire traitée comme aval',
        'كابينة تُعامل كمصب',
    )
    add(
        '自环',
        'Bucle sobre sí mismo',
        'Bucle sobre sí mismo',
        'Boucle sur soi',
        'حلقة ذاتية',
    )
    add(
        '未挂上的线',
        'Unattached line',
        'Línea no conectada',
        'Ligne non rattachée',
        'خط غير موصول',
    )
    add(
        '未挂上的点',
        'Unattached point',
        'Punto no conectado',
        'Point non rattaché',
        'نقطة غير موصولة',
    )
    add(
        '光交无出线',
        'Armario sin línea de salida',
        'Armario sin línea de salida',
        'Armoire sans ligne sortante',
        'كابينة بلا خط خارج',
    )
    add(
        '接头名称不合规',
        'Nombre de empalme no válido',
        'Nombre de empalme no válido',
        "Nom d'épissure non conforme",
        'اسم الوصلة غير مطابق',
    )
    add(
        'CODE重复',
        'CODE repetido',
        'CODE repetido',
        'CODE en double',
        'رمز مكرر',
    )
    add(
        '城市PM不一致',
        'Ciudad o PM no coinciden',
        'Ciudad o PM no coinciden',
        'Ville ou PM différent',
        'المدينة أو PM غير متطابق',
    )
    add(
        '接头无配线',
        'Empalme sin distribución',
        'Empalme sin distribución',
        'Épissure sans distribution',
        'وصلة بلا توزيع',
    )
    add(
        '线方向反了',
        'Line direction reversed',
        'Dirección de línea invertida',
        'Sens de ligne inversé',
        'اتجاه الخط معكوس',
    )
    add(
        '伪成环',
        'Pseudo-loop',
        'Falso bucle',
        'Fausse boucle',
        'حلقة زائفة',
    )
    add(
        '方向无法判断',
        'Direction undecided',
        'Dirección sin decidir',
        'Sens indécis',
        'اتجاه غير محسوم',
    )
    add(
        '方向冲突',
        'Conflicto de dirección',
        'Conflicto de dirección',
        'Conflit de sens',
        'تعارض الاتجاه',
    )
    add(
        '角色异常',
        'Rol inesperado',
        'Rol inesperado',
        'Rôle inattendu',
        'دور غير متوقع',
    )
    add(
        '分纤盒户数为0',
        'La caja FAT tiene 0 hogares',
        'La caja FAT tiene 0 hogares',
        'Le boîtier FAT a 0 foyers',
        'عدد المشتركين في العلبة صفر',
    )
    add(
        '链路排名平局',
        'Empate en el rango del camino',
        'Empate en el rango del camino',
        'Égalité de rang de chemin',
        'تعادل في ترتيب المسار',
    )
    add(
        '分纤盒无进线',
        'Caja FAT sin línea de entrada',
        'Caja FAT sin línea de entrada',
        'Boîtier FAT sans ligne entrante',
        'علبة بلا خط داخل',
    )
    add(
        '接头无进线',
        'Empalme sin línea de entrada',
        'Empalme sin línea de entrada',
        'Épissure sans ligne entrante',
        'وصلة بلا خط داخل',
    )
    add(
        '用户点无皮线',
        'Punto de usuario sin acometida',
        'Punto de usuario sin acometida',
        'Point usager sans branchement',
        'نقطة مستخدم بلا كبل إسقاط',
    )
    add(
        '光缆一端空',
        'Cable con un extremo abierto',
        'Cable con un extremo abierto',
        'Câble avec une extrémité ouverte',
        'كابل طرفه واحد فارغ',
    )
    add(
        '光缆两端空',
        'Cable con ambos extremos abiertos',
        'Cable con ambos extremos abiertos',
        'Câble avec les deux extrémités ouvertes',
        'كابل طرفاه فارغان',
    )
    add(
        '光缆端点非法',
        'Extremo de cable no válido',
        'Extremo de cable no válido',
        'Extrémité de câble illégale',
        'طرف كابل غير مسموح',
    )
    add(
        '光缆未从光交挂上',
        'Cable no alcanzado desde el armario',
        'Cable no alcanzado desde el armario',
        "Câble non atteint depuis l'armoire",
        'كابل لم يُوصل من الكابينة',
    )
    add(
        '皮线一端空',
        'Acometida con un extremo abierto',
        'Acometida con un extremo abierto',
        'Branchement avec une extrémité ouverte',
        'كبل إسقاط طرفه واحد فارغ',
    )
    add(
        '皮线两端空',
        'Acometida con ambos extremos abiertos',
        'Acometida con ambos extremos abiertos',
        'Branchement avec les deux extrémités ouvertes',
        'كبل إسقاط طرفاه فارغان',
    )
    add(
        '皮线端点非法',
        'Extremo de acometida no válido',
        'Extremo de acometida no válido',
        'Extrémité de branchement illégale',
        'طرف كبل إسقاط غير مسموح',
    )
    add(
        '设备点重叠',
        'Puntos de equipo superpuestos',
        'Puntos de equipo superpuestos',
        "Points d'équipement superposés",
        'نقاط تجهيز متداخلة',
    )
    add(
        '端点附近多个设备',
        'Varios equipos cerca de un extremo',
        'Varios equipos cerca de un extremo',
        "Plusieurs équipements près d'une extrémité",
        'عدة تجهيزات قرب طرف',
    )
    add(
        'CODE为空',
        'CODE vacío',
        'CODE vacío',
        'CODE vide',
        'الرمز فارغ',
    )
    add(
        'bucket 是产出时的 hard/soft/warn；未标 soft 的旧结果按 kind 再拆。',
        'bucket 是产出时的 hard/soft/warn；未标 soft 的旧结果按 kind 再拆。',
        'bucket 是产出时的 hard/soft/warn；未标 soft 的旧结果按 kind 再拆。',
        'bucket 是产出时的 hard/soft/warn；未标 soft 的旧结果按 kind 再拆。',
        'bucket 是产出时的 hard/soft/warn；未标 soft 的旧结果按 kind 再拆。',
    )
    add(
        '返回 (硬错误, 软错误, 警告)。赋值/命名仍只产 hard+warn 时，这里按 kind 拆开。',
        '返回 (硬错误, 软错误, 警告)。赋值/命名仍只产 hard+warn 时，这里按 kind 拆开。',
        '返回 (硬错误, 软错误, 警告)。赋值/命名仍只产 hard+warn 时，这里按 kind 拆开。',
        '返回 (硬错误, 软错误, 警告)。赋值/命名仍只产 hard+warn 时，这里按 kind 拆开。',
        '返回 (硬错误, 软错误, 警告)。赋值/命名仍只产 hard+warn 时，这里按 kind 拆开。',
    )
    add(
        '曲线先拉直，多段线只留最长一段。',
        '曲线先拉直，多段线只留最长一段。',
        '曲线先拉直，多段线只留最长一段。',
        '曲线先拉直，多段线只留最长一段。',
        '曲线先拉直，多段线只留最长一段。',
    )
    add(
        '折线沿线长度一半，点一定在这段折线上。不用两端连线中点。',
        '折线沿线长度一半，点一定在这段折线上。不用两端连线中点。',
        '折线沿线长度一半，点一定在这段折线上。不用两端连线中点。',
        '折线沿线长度一半，点一定在这段折线上。不用两端连线中点。',
        '折线沿线长度一半，点一定在这段折线上。不用两端连线中点。',
    )
    add(
        '该条线自己的几何中点：先拉直，多段线只取最长一段，沿线一半，点在线上。',
        '该条线自己的几何中点：先拉直，多段线只取最长一段，沿线一半，点在线上。',
        '该条线自己的几何中点：先拉直，多段线只取最长一段，沿线一半，点在线上。',
        '该条线自己的几何中点：先拉直，多段线只取最长一段，沿线一半，点在线上。',
        '该条线自己的几何中点：先拉直，多段线只取最长一段，沿线一半，点在线上。',
    )
    add(
        '把点吸附回该条线，避免坐标变换后离开线。',
        '把点吸附回该条线，避免坐标变换后离开线。',
        '把点吸附回该条线，避免坐标变换后离开线。',
        '把点吸附回该条线，避免坐标变换后离开线。',
        '把点吸附回该条线，避免坐标变换后离开线。',
    )
    add(
        '写入前检查字段：CODE 只能写进文本字段，且不能超过字段长度（Shapefile 保存时会截断）。',
        '写入前检查字段：CODE 只能写进文本字段，且不能超过字段长度（Shapefile 保存时会截断）。',
        '写入前检查字段：CODE 只能写进文本字段，且不能超过字段长度（Shapefile 保存时会截断）。',
        '写入前检查字段：CODE 只能写进文本字段，且不能超过字段长度（Shapefile 保存时会截断）。',
        '写入前检查字段：CODE 只能写进文本字段，且不能超过字段长度（Shapefile 保存时会截断）。',
    )
    add(
        '新 CODE 和图层里其它要素已有的 CODE 相同（这次没有重写的要素）。',
        '新 CODE 和图层里其它要素已有的 CODE 相同（这次没有重写的要素）。',
        '新 CODE 和图层里其它要素已有的 CODE 相同（这次没有重写的要素）。',
        '新 CODE 和图层里其它要素已有的 CODE 相同（这次没有重写的要素）。',
        '新 CODE 和图层里其它要素已有的 CODE 相同（这次没有重写的要素）。',
    )
    add(
        'NTAL 写入',
        'NTAL 写入',
        'NTAL 写入',
        'NTAL 写入',
        'NTAL 写入',
    )
    add(
        '通用线方向_起点终点',
        'Free-start line direction_Start and end',
        'Dirección de líneas, inicio y final',
        'Sens des lignes, départ et fin',
        'اتجاه الخطوط، البداية والنهاية',
    )
    add(
        '只认插件自己建的临时点层。旧工程里没打标记的，按「内存图层 + 在结果组里」认。',
        '只认插件自己建的临时点层。旧工程里没打标记的，按「内存图层 + 在结果组里」认。',
        '只认插件自己建的临时点层。旧工程里没打标记的，按「内存图层 + 在结果组里」认。',
        '只认插件自己建的临时点层。旧工程里没打标记的，按「内存图层 + 在结果组里」认。',
        '只认插件自己建的临时点层。旧工程里没打标记的，按「内存图层 + 在结果组里」认。',
    )
    add(
        '清掉同一来源上次留下的临时点层，避免已修好的问题还挂在组里。',
        '清掉同一来源上次留下的临时点层，避免已修好的问题还挂在组里。',
        '清掉同一来源上次留下的临时点层，避免已修好的问题还挂在组里。',
        '清掉同一来源上次留下的临时点层，避免已修好的问题还挂在组里。',
        '清掉同一来源上次留下的临时点层，避免已修好的问题还挂在组里。',
    )
    add(
        '该条线自己的几何中点。算出后转到工程 CRS，再吸附回这条线。',
        '该条线自己的几何中点。算出后转到工程 CRS，再吸附回这条线。',
        '该条线自己的几何中点。算出后转到工程 CRS，再吸附回这条线。',
        '该条线自己的几何中点。算出后转到工程 CRS，再吸附回这条线。',
        '该条线自己的几何中点。算出后转到工程 CRS，再吸附回这条线。',
    )
    add(
        '同一位置只留一个临时点。地图用一行短名，完整标题放进 detail。',
        '同一位置只留一个临时点。地图用一行短名，完整标题放进 detail。',
        '同一位置只留一个临时点。地图用一行短名，完整标题放进 detail。',
        '同一位置只留一个临时点。地图用一行短名，完整标题放进 detail。',
        '同一位置只留一个临时点。地图用一行短名，完整标题放进 detail。',
    )
    add(
        '反了',
        'Reversed',
        'Invertida',
        'Inversé',
        'معكوس',
    )
    add(
        '歧义',
        '歧义',
        '歧义',
        '歧义',
        '歧义',
    )
    add(
        '未挂上',
        'Unattached',
        'Sin conectar',
        'Non rattaché',
        'غير متصل',
    )
    add(
        '分叉',
        '分叉',
        '分叉',
        '分叉',
        '分叉',
    )
    add(
        '多进线',
        '多进线',
        '多进线',
        '多进线',
        '多进线',
    )
    add(
        '主干分叉',
        '主干分叉',
        '主干分叉',
        '主干分叉',
        '主干分叉',
    )
    add(
        '光交下游',
        '光交下游',
        '光交下游',
        '光交下游',
        '光交下游',
    )
    add(
        '重复皮线',
        '重复皮线',
        '重复皮线',
        '重复皮线',
        '重复皮线',
    )
    add(
        '多盒覆盖',
        '多盒覆盖',
        '多盒覆盖',
        '多盒覆盖',
        '多盒覆盖',
    )
    add(
        '无皮线',
        '无皮线',
        '无皮线',
        '无皮线',
        '无皮线',
    )
    add(
        '无配线',
        '无配线',
        '无配线',
        '无配线',
        '无配线',
    )
    add(
        '问题',
        'Issue',
        'Problema',
        'Problème',
        'مشكلة',
    )
    add(
        '硬错误_',
        '硬错误_',
        '硬错误_',
        '硬错误_',
        '硬错误_',
    )
    add(
        '软错误_',
        '软错误_',
        '软错误_',
        '软错误_',
        '软错误_',
    )
    add(
        '警告_',
        '警告_',
        '警告_',
        '警告_',
        '警告_',
    )
    add(
        ' 户数={}',
        ' 户数={}',
        ' 户数={}',
        ' 户数={}',
        ' 户数={}',
    )
    add(
        '{} 没有字段 {}',
        '{} 没有字段 {}',
        '{} 没有字段 {}',
        '{} 没有字段 {}',
        '{} 没有字段 {}',
    )
    add(
        '{} 写入异常：{}',
        '{} 写入异常：{}',
        '{} 写入异常：{}',
        '{} 写入异常：{}',
        '{} 写入异常：{}',
    )
    add(
        '{} #{} 写入失败',
        '{} #{} 写入失败',
        '{} #{} 写入失败',
        '{} #{} 写入失败',
        '{} #{} 写入失败',
    )
    add(
        '长链路逐点递归，临时放宽递归上限。',
        '长链路逐点递归，临时放宽递归上限。',
        '长链路逐点递归，临时放宽递归上限。',
        '长链路逐点递归，临时放宽递归上限。',
        '长链路逐点递归，临时放宽递归上限。',
    )
    add(
        '规则树里关掉的分类也打开。只改渲染器副本。',
        '规则树里关掉的分类也打开。只改渲染器副本。',
        '规则树里关掉的分类也打开。只改渲染器副本。',
        '规则树里关掉的分类也打开。只改渲染器副本。',
        '规则树里关掉的分类也打开。只改渲染器副本。',
    )
    add(
        '副本上打开全部分类。图层面板的显示勾选不参与筛选。',
        '副本上打开全部分类。图层面板的显示勾选不参与筛选。',
        '副本上打开全部分类。图层面板的显示勾选不参与筛选。',
        '副本上打开全部分类。图层面板的显示勾选不参与筛选。',
        '副本上打开全部分类。图层面板的显示勾选不参与筛选。',
    )
    add(
        '配置里勾了分类筛选（不是「全部」）。',
        '配置里勾了分类筛选（不是「全部」）。',
        '配置里勾了分类筛选（不是「全部」）。',
        '配置里勾了分类筛选（不是「全部」）。',
        '配置里勾了分类筛选（不是「全部」）。',
    )
    add(
        '带工程/图层表达式上下文，规则里用 @project_*、@layer_* 变量时才判得对。',
        '带工程/图层表达式上下文，规则里用 @project_*、@layer_* 变量时才判得对。',
        '带工程/图层表达式上下文，规则里用 @project_*、@layer_* 变量时才判得对。',
        '带工程/图层表达式上下文，规则里用 @project_*、@layer_* 变量时才判得对。',
        '带工程/图层表达式上下文，规则里用 @project_*、@layer_* 变量时才判得对。',
    )
    add(
        '要素自己的分类名。未筛分类时为空。',
        '要素自己的分类名。未筛分类时为空。',
        '要素自己的分类名。未筛分类时为空。',
        '要素自己的分类名。未筛分类时为空。',
        '要素自己的分类名。未筛分类时为空。',
    )
    add(
        '从光交往用户检查线数字化方向，并报告主干配线的结构硬错误。先出临时点，窗口不挡地图，再全部翻转或翻转勾选。',
        '从光交往用户检查线数字化方向，并报告主干配线的结构硬错误。先出临时点，窗口不挡地图，再全部翻转或翻转勾选。',
        '从光交往用户检查线数字化方向，并报告主干配线的结构硬错误。先出临时点，窗口不挡地图，再全部翻转或翻转勾选。',
        '从光交往用户检查线数字化方向，并报告主干配线的结构硬错误。先出临时点，窗口不挡地图，再全部翻转或翻转勾选。',
        '从光交往用户检查线数字化方向，并报告主干配线的结构硬错误。先出临时点，窗口不挡地图，再全部翻转或翻转勾选。',
    )
    add(
        '只倒顶点顺序。保留 Z/M 和圆弧，不打散曲线。',
        '只倒顶点顺序。保留 Z/M 和圆弧，不打散曲线。',
        '只倒顶点顺序。保留 Z/M 和圆弧，不打散曲线。',
        '只倒顶点顺序。保留 Z/M 和圆弧，不打散曲线。',
        '只倒顶点顺序。保留 Z/M 和圆弧，不打散曲线。',
    )
    add(
        '阶段进度。刷新间隔约 0.25 秒，不在每个要素上重绘。',
        '阶段进度。刷新间隔约 0.25 秒，不在每个要素上重绘。',
        '阶段进度。刷新间隔约 0.25 秒，不在每个要素上重绘。',
        '阶段进度。刷新间隔约 0.25 秒，不在每个要素上重绘。',
        '阶段进度。刷新间隔约 0.25 秒，不在每个要素上重绘。',
    )
    add(
        'prepared：全面检测已经采集好的点线，传进来就不再读一遍图层。',
        'prepared：全面检测已经采集好的点线，传进来就不再读一遍图层。',
        'prepared：全面检测已经采集好的点线，传进来就不再读一遍图层。',
        'prepared：全面检测已经采集好的点线，传进来就不再读一遍图层。',
        'prepared：全面检测已经采集好的点线，传进来就不再读一遍图层。',
    )
    add(
        '（空）',
        '(blank)',
        '(vacío)',
        '(vide)',
        '(فارغ)',
    )
    add(
        '通用线方向：自选一个起点和多个线图层，端点在容差内才相接，断口停下。不读正式图层配置。',
        '通用线方向：自选一个起点和多个线图层，端点在容差内才相接，断口停下。不读正式图层配置。',
        '通用线方向：自选一个起点和多个线图层，端点在容差内才相接，断口停下。不读正式图层配置。',
        '通用线方向：自选一个起点和多个线图层，端点在容差内才相接，断口停下。不读正式图层配置。',
        '通用线方向：自选一个起点和多个线图层，端点在容差内才相接，断口停下。不读正式图层配置。',
    )
    add(
        '终点贴在线的中间、但没贴到这条线任一端点。\n\n    这种终点不在两根线的接头上，不能把环断开。\n    ',
        '终点贴在线的中间、但没贴到这条线任一端点。\n\n    这种终点不在两根线的接头上，不能把环断开。\n    ',
        '终点贴在线的中间、但没贴到这条线任一端点。\n\n    这种终点不在两根线的接头上，不能把环断开。\n    ',
        '终点贴在线的中间、但没贴到这条线任一端点。\n\n    这种终点不在两根线的接头上，不能把环断开。\n    ',
        '终点贴在线的中间、但没贴到这条线任一端点。\n\n    这种终点不在两根线的接头上，不能把环断开。\n    ',
    )
    add(
        '方向反了',
        'Reversed',
        'Invertida',
        'Inversée',
        'الاتجاه معكوس',
    )
    add(
        '接头第五段/第六段，以及分纤盒配线链路排名。户数多的号小，户数相同则更长的号小。',
        '接头第五段/第六段，以及分纤盒配线链路排名。户数多的号小，户数相同则更长的号小。',
        '接头第五段/第六段，以及分纤盒配线链路排名。户数多的号小，户数相同则更长的号小。',
        '接头第五段/第六段，以及分纤盒配线链路排名。户数多的号小，户数相同则更长的号小。',
        '接头第五段/第六段，以及分纤盒配线链路排名。户数多的号小，户数相同则更长的号小。',
    )
    add(
        '每个接头的每条出线走到串尾 = 一条链路。没有配线不占接头编号。',
        '每个接头的每条出线走到串尾 = 一条链路。没有配线不占接头编号。',
        '每个接头的每条出线走到串尾 = 一条链路。没有配线不占接头编号。',
        '每个接头的每条出线走到串尾 = 一条链路。没有配线不占接头编号。',
        '每个接头的每条出线走到串尾 = 一条链路。没有配线不占接头编号。',
    )
    add(
        '每个接头自己接出去的配线户数，不含下接接头。户数为 0 记硬错误。',
        '每个接头自己接出去的配线户数，不含下接接头。户数为 0 记硬错误。',
        '每个接头自己接出去的配线户数，不含下接接头。户数为 0 记硬错误。',
        '每个接头自己接出去的配线户数，不含下接接头。户数为 0 记硬错误。',
        '每个接头自己接出去的配线户数，不含下接接头。户数为 0 记硬错误。',
    )
    add(
        '光缆两端角色：只看端点吸附到的点，不看线中间折点。',
        '光缆两端角色：只看端点吸附到的点，不看线中间折点。',
        '光缆两端角色：只看端点吸附到的点，不看线中间折点。',
        '光缆两端角色：只看端点吸附到的点，不看线中间折点。',
        '光缆两端角色：只看端点吸附到的点，不看线中间折点。',
    )
    add(
        '皮线。一头空 / 两头空都是软错误。合法两端对由组网方案决定。',
        '皮线。一头空 / 两头空都是软错误。合法两端对由组网方案决定。',
        '皮线。一头空 / 两头空都是软错误。合法两端对由组网方案决定。',
        '皮线。一头空 / 两头空都是软错误。合法两端对由组网方案决定。',
        '皮线。一头空 / 两头空都是软错误。合法两端对由组网方案决定。',
    )
    add(
        '吸附光缆两端并判定主干/配线。歧义进硬错误。',
        '吸附光缆两端并判定主干/配线。歧义进硬错误。',
        '吸附光缆两端并判定主干/配线。歧义进硬错误。',
        '吸附光缆两端并判定主干/配线。歧义进硬错误。',
        '吸附光缆两端并判定主干/配线。歧义进硬错误。',
    )
    add(
        '每个下拉功能各自一份方案。组网结构固定；变的是赋值怎么写、后三段怎么编号。',
        '每个下拉功能各自一份方案。组网结构固定；变的是赋值怎么写、后三段怎么编号。',
        '每个下拉功能各自一份方案。组网结构固定；变的是赋值怎么写、后三段怎么编号。',
        '每个下拉功能各自一份方案。组网结构固定；变的是赋值怎么写、后三段怎么编号。',
        '每个下拉功能各自一份方案。组网结构固定；变的是赋值怎么写、后三段怎么编号。',
    )
    add(
        '赋值·皮线',
        'Relleno · acometida',
        'Relleno · acometida',
        'Remplissage · branchement',
        'ملء · كبل الإسقاط',
    )
    add(
        '赋值·分纤盒',
        'Relleno · caja FAT',
        'Relleno · caja FAT',
        'Remplissage · FAT',
        'ملء · علبة التوزيع',
    )
    add(
        '赋值·主干配线',
        'Relleno · alimentador y distribución',
        'Relleno · alimentador y distribución',
        'Remplissage · alimentation et distribution',
        'ملء · التغذية والتوزيع',
    )
    add(
        '命名·接头',
        'Nombre · empalme',
        'Nombre · empalme',
        'Nom · épissure',
        'تسمية · وصلة',
    )
    add(
        '命名·分纤盒',
        'Nombre · caja FAT',
        'Nombre · caja FAT',
        'Nom · FAT',
        'تسمية · علبة التوزيع',
    )
    add(
        '命名·主干配线',
        'Nombre · alimentador y distribución',
        'Nombre · alimentador y distribución',
        'Nom · alimentation et distribution',
        'تسمية · التغذية والتوزيع',
    )
    add(
        '当前',
        '当前',
        '当前',
        '当前',
        '当前',
    )
    add(
        '旧户数',
        '旧户数',
        '旧户数',
        '旧户数',
        '旧户数',
    )
    add(
        '旧配置只有一个 scheme / 累加勾选，拆到六个功能。未知 id 回落到当前。',
        '旧配置只有一个 scheme / 累加勾选，拆到六个功能。未知 id 回落到当前。',
        '旧配置只有一个 scheme / 累加勾选，拆到六个功能。未知 id 回落到当前。',
        '旧配置只有一个 scheme / 累加勾选，拆到六个功能。未知 id 回落到当前。',
        '旧配置只有一个 scheme / 累加勾选，拆到六个功能。未知 id 回落到当前。',
    )
    add(
        '当前：抄用户户数',
        '当前：抄用户户数',
        '当前：抄用户户数',
        '当前：抄用户户数',
        '当前：抄用户户数',
    )
    add(
        '读用户点户数，写到连上的皮线。一个用户接多个分纤盒时该皮线不写。没挂上的皮线保持原值。',
        '读用户点户数，写到连上的皮线。一个用户接多个分纤盒时该皮线不写。没挂上的皮线保持原值。',
        '读用户点户数，写到连上的皮线。一个用户接多个分纤盒时该皮线不写。没挂上的皮线保持原值。',
        '读用户点户数，写到连上的皮线。一个用户接多个分纤盒时该皮线不写。没挂上的皮线保持原值。',
        '读用户点户数，写到连上的皮线。一个用户接多个分纤盒时该皮线不写。没挂上的皮线保持原值。',
    )
    add(
        '每条皮线写 1',
        '每条皮线写 1',
        '每条皮线写 1',
        '每条皮线写 1',
        '每条皮线写 1',
    )
    add(
        '合格皮线一律写 1，不读用户点户数字段的数值。一个用户接多个分纤盒时仍不写。没挂上的皮线保持原值。',
        '合格皮线一律写 1，不读用户点户数字段的数值。一个用户接多个分纤盒时仍不写。没挂上的皮线保持原值。',
        '合格皮线一律写 1，不读用户点户数字段的数值。一个用户接多个分纤盒时仍不写。没挂上的皮线保持原值。',
        '合格皮线一律写 1，不读用户点户数字段的数值。一个用户接多个分纤盒时仍不写。没挂上的皮线保持原值。',
        '合格皮线一律写 1，不读用户点户数字段的数值。一个用户接多个分纤盒时仍不写。没挂上的皮线保持原值。',
    )
    add(
        '多盒覆盖也写',
        '多盒覆盖也写',
        '多盒覆盖也写',
        '多盒覆盖也写',
        '多盒覆盖也写',
    )
    add(
        '仍抄用户点户数。同一用户接到多个分纤盒时，每条合格皮线都写（各写一遍该用户户数）。同盒重复皮线仍不写。',
        '仍抄用户点户数。同一用户接到多个分纤盒时，每条合格皮线都写（各写一遍该用户户数）。同盒重复皮线仍不写。',
        '仍抄用户点户数。同一用户接到多个分纤盒时，每条合格皮线都写（各写一遍该用户户数）。同盒重复皮线仍不写。',
        '仍抄用户点户数。同一用户接到多个分纤盒时，每条合格皮线都写（各写一遍该用户户数）。同盒重复皮线仍不写。',
        '仍抄用户点户数。同一用户接到多个分纤盒时，每条合格皮线都写（各写一遍该用户户数）。同盒重复皮线仍不写。',
    )
    add(
        '当前：皮线户数合计',
        '当前：皮线户数合计',
        '当前：皮线户数合计',
        '当前：皮线户数合计',
        '当前：皮线户数合计',
    )
    add(
        '分纤盒户数 = 一端吸到该盒的皮线户数之和。先核用户点总户数和皮线字段总户数，对不上整批不写。',
        '分纤盒户数 = 一端吸到该盒的皮线户数之和。先核用户点总户数和皮线字段总户数，对不上整批不写。',
        '分纤盒户数 = 一端吸到该盒的皮线户数之和。先核用户点总户数和皮线字段总户数，对不上整批不写。',
        '分纤盒户数 = 一端吸到该盒的皮线户数之和。先核用户点总户数和皮线字段总户数，对不上整批不写。',
        '分纤盒户数 = 一端吸到该盒的皮线户数之和。先核用户点总户数和皮线字段总户数，对不上整批不写。',
    )
    add(
        '按皮线条数',
        '按皮线条数',
        '按皮线条数',
        '按皮线条数',
        '按皮线条数',
    )
    add(
        '分纤盒写入所出皮线的条数，不加户数。仍先核用户点总户数和皮线字段总户数，对不上整批不写。',
        '分纤盒写入所出皮线的条数，不加户数。仍先核用户点总户数和皮线字段总户数，对不上整批不写。',
        '分纤盒写入所出皮线的条数，不加户数。仍先核用户点总户数和皮线字段总户数，对不上整批不写。',
        '分纤盒写入所出皮线的条数，不加户数。仍先核用户点总户数和皮线字段总户数，对不上整批不写。',
        '分纤盒写入所出皮线的条数，不加户数。仍先核用户点总户数和皮线字段总户数，对不上整批不写。',
    )
    add(
        '皮线合计（不核总户数）',
        '皮线合计（不核总户数）',
        '皮线合计（不核总户数）',
        '皮线合计（不核总户数）',
        '皮线合计（不核总户数）',
    )
    add(
        '仍按所出皮线户数加总。用户点总户数和皮线字段对不上只报软错误，其余分纤盒照写。',
        '仍按所出皮线户数加总。用户点总户数和皮线字段对不上只报软错误，其余分纤盒照写。',
        '仍按所出皮线户数加总。用户点总户数和皮线字段对不上只报软错误，其余分纤盒照写。',
        '仍按所出皮线户数加总。用户点总户数和皮线字段对不上只报软错误，其余分纤盒照写。',
        '仍按所出皮线户数加总。用户点总户数和皮线字段对不上只报软错误，其余分纤盒照写。',
    )
    add(
        '当前：配线只写本盒',
        '当前：配线只写本盒',
        '当前：配线只写本盒',
        '当前：配线只写本盒',
        '当前：配线只写本盒',
    )
    add(
        '主干不写户数。配线只写到达的那一个分纤盒。接头-盒1-盒2 时，第一段配线只写盒1。',
        '主干不写户数。配线只写到达的那一个分纤盒。接头-盒1-盒2 时，第一段配线只写盒1。',
        '主干不写户数。配线只写到达的那一个分纤盒。接头-盒1-盒2 时，第一段配线只写盒1。',
        '主干不写户数。配线只写到达的那一个分纤盒。接头-盒1-盒2 时，第一段配线只写盒1。',
        '主干不写户数。配线只写到达的那一个分纤盒。接头-盒1-盒2 时，第一段配线只写盒1。',
    )
    add(
        '下游累加（主干也写）',
        '下游累加（主干也写）',
        '下游累加（主干也写）',
        '下游累加（主干也写）',
        '下游累加（主干也写）',
    )
    add(
        '按下游分纤盒户数累加，主干也写。组网不变。命名不受此项影响。',
        '按下游分纤盒户数累加，主干也写。组网不变。命名不受此项影响。',
        '按下游分纤盒户数累加，主干也写。组网不变。命名不受此项影响。',
        '按下游分纤盒户数累加，主干也写。组网不变。命名不受此项影响。',
        '按下游分纤盒户数累加，主干也写。组网不变。命名不受此项影响。',
    )
    add(
        '配线下游累加（主干不写）',
        '配线下游累加（主干不写）',
        '配线下游累加（主干不写）',
        '配线下游累加（主干不写）',
        '配线下游累加（主干不写）',
    )
    add(
        '配线按下游分纤盒户数累加。主干仍不写。组网不变。命名不受此项影响。',
        '配线按下游分纤盒户数累加。主干仍不写。组网不变。命名不受此项影响。',
        '配线按下游分纤盒户数累加。主干仍不写。组网不变。命名不受此项影响。',
        '配线按下游分纤盒户数累加。主干仍不写。组网不变。命名不受此项影响。',
        '配线按下游分纤盒户数累加。主干仍不写。组网不变。命名不受此项影响。',
    )
    add(
        '当前：分叉另开第五段',
        '当前：分叉另开第五段',
        '当前：分叉另开第五段',
        '当前：分叉另开第五段',
        '当前：分叉另开第五段',
    )
    add(
        '一条链：第五段固定 01',
        '一条链：第五段固定 01',
        '一条链：第五段固定 01',
        '一条链：第五段固定 01',
        '一条链：第五段固定 01',
    )
    add(
        '第四段与当前相同。整条 ODF 上所有接头第五段都是 01，第六段按主干走到的顺序 01、02、03（分叉也接着编，不新开第五段）。',
        '第四段与当前相同。整条 ODF 上所有接头第五段都是 01，第六段按主干走到的顺序 01、02、03（分叉也接着编，不新开第五段）。',
        '第四段与当前相同。整条 ODF 上所有接头第五段都是 01，第六段按主干走到的顺序 01、02、03（分叉也接着编，不新开第五段）。',
        '第四段与当前相同。整条 ODF 上所有接头第五段都是 01，第六段按主干走到的顺序 01、02、03（分叉也接着编，不新开第五段）。',
        '第四段与当前相同。整条 ODF 上所有接头第五段都是 01，第六段按主干走到的顺序 01、02、03（分叉也接着编，不新开第五段）。',
    )
    add(
        '每个接头一个第五段',
        '每个接头一个第五段',
        '每个接头一个第五段',
        '每个接头一个第五段',
        '每个接头一个第五段',
    )
    add(
        '第四段与当前相同。每走到一个接头就新开第五段（01、02、03…），第六段固定 01。分叉仍按户数、到下一接头长度决定先后。',
        '第四段与当前相同。每走到一个接头就新开第五段（01、02、03…），第六段固定 01。分叉仍按户数、到下一接头长度决定先后。',
        '第四段与当前相同。每走到一个接头就新开第五段（01、02、03…），第六段固定 01。分叉仍按户数、到下一接头长度决定先后。',
        '第四段与当前相同。每走到一个接头就新开第五段（01、02、03…），第六段固定 01。分叉仍按户数、到下一接头长度决定先后。',
        '第四段与当前相同。每走到一个接头就新开第五段（01、02、03…），第六段固定 01。分叉仍按户数、到下一接头长度决定先后。',
    )
    add(
        'ODF 先按出线角度',
        'ODF 先按出线角度',
        'ODF 先按出线角度',
        'ODF 先按出线角度',
        'ODF 先按出线角度',
    )
    add(
        '后两段与「当前：分叉另开第五段」相同。第四段先比出线角度（参数里的方向/起始角），角度相同再比第一段主干长短。',
        '后两段与「当前：分叉另开第五段」相同。第四段先比出线角度（参数里的方向/起始角），角度相同再比第一段主干长短。',
        '后两段与「当前：分叉另开第五段」相同。第四段先比出线角度（参数里的方向/起始角），角度相同再比第一段主干长短。',
        '后两段与「当前：分叉另开第五段」相同。第四段先比出线角度（参数里的方向/起始角），角度相同再比第一段主干长短。',
        '后两段与「当前：分叉另开第五段」相同。第四段先比出线角度（参数里的方向/起始角），角度相同再比第一段主干长短。',
    )
    add(
        '当前：接在接头第五段后面',
        '当前：接在接头第五段后面',
        '当前：接在接头第五段后面',
        '当前：接在接头第五段后面',
        '当前：接在接头第五段后面',
    )
    add(
        '跟接头共用第五段',
        '跟接头共用第五段',
        '跟接头共用第五段',
        '跟接头共用第五段',
        '跟接头共用第五段',
    )
    add(
        '分纤盒第五段 = 所接接头 CODE 的第五段。该接头下的配线按户数、到首盒线长排，第六段从 01 起连续编（多条配线接着编，不每条链都从 01 起）。',
        '分纤盒第五段 = 所接接头 CODE 的第五段。该接头下的配线按户数、到首盒线长排，第六段从 01 起连续编（多条配线接着编，不每条链都从 01 起）。',
        '分纤盒第五段 = 所接接头 CODE 的第五段。该接头下的配线按户数、到首盒线长排，第六段从 01 起连续编（多条配线接着编，不每条链都从 01 起）。',
        '分纤盒第五段 = 所接接头 CODE 的第五段。该接头下的配线按户数、到首盒线长排，第六段从 01 起连续编（多条配线接着编，不每条链都从 01 起）。',
        '分纤盒第五段 = 所接接头 CODE 的第五段。该接头下的配线按户数、到首盒线长排，第六段从 01 起连续编（多条配线接着编，不每条链都从 01 起）。',
    )
    add(
        '每个接头从 01 起',
        '每个接头从 01 起',
        '每个接头从 01 起',
        '每个接头从 01 起',
        '每个接头从 01 起',
    )
    add(
        '每个接头自己的配线单独排，第五段从 01 起，不看同 ODF 其它接头用到几。每条链第六段从 01 起。',
        '每个接头自己的配线单独排，第五段从 01 起，不看同 ODF 其它接头用到几。每条链第六段从 01 起。',
        '每个接头自己的配线单独排，第五段从 01 起，不看同 ODF 其它接头用到几。每条链第六段从 01 起。',
        '每个接头自己的配线单独排，第五段从 01 起，不看同 ODF 其它接头用到几。每条链第六段从 01 起。',
        '每个接头自己的配线单独排，第五段从 01 起，不看同 ODF 其它接头用到几。每条链第六段从 01 起。',
    )
    add(
        '第六段整条 ODF 连续',
        '第六段整条 ODF 连续',
        '第六段整条 ODF 连续',
        '第六段整条 ODF 连续',
        '第六段整条 ODF 连续',
    )
    add(
        '第五段仍从该 ODF 接头第五段最大值 +1 起、按户数排。第六段不按链归零，整条 ODF 从 01 一直加下去。',
        '第五段仍从该 ODF 接头第五段最大值 +1 起、按户数排。第六段不按链归零，整条 ODF 从 01 一直加下去。',
        '第五段仍从该 ODF 接头第五段最大值 +1 起、按户数排。第六段不按链归零，整条 ODF 从 01 一直加下去。',
        '第五段仍从该 ODF 接头第五段最大值 +1 起、按户数排。第六段不按链归零，整条 ODF 从 01 一直加下去。',
        '第五段仍从该 ODF 接头第五段最大值 +1 起、按户数排。第六段不按链归零，整条 ODF 从 01 一直加下去。',
    )
    add(
        '当前：抄到达对象并换前缀',
        '当前：抄到达对象并换前缀',
        '当前：抄到达对象并换前缀',
        '当前：抄到达对象并换前缀',
        '当前：抄到达对象并换前缀',
    )
    add(
        '顺着光交往外走。主干抄到达接头的 CODE，配线抄到达分纤盒的 CODE，只换光缆前缀和主窗口城市/PM。到达对象城市/PM 不一致不写。',
        '顺着光交往外走。主干抄到达接头的 CODE，配线抄到达分纤盒的 CODE，只换光缆前缀和主窗口城市/PM。到达对象城市/PM 不一致不写。',
        '顺着光交往外走。主干抄到达接头的 CODE，配线抄到达分纤盒的 CODE，只换光缆前缀和主窗口城市/PM。到达对象城市/PM 不一致不写。',
        '顺着光交往外走。主干抄到达接头的 CODE，配线抄到达分纤盒的 CODE，只换光缆前缀和主窗口城市/PM。到达对象城市/PM 不一致不写。',
        '顺着光交往外走。主干抄到达接头的 CODE，配线抄到达分纤盒的 CODE，只换光缆前缀和主窗口城市/PM。到达对象城市/PM 不一致不写。',
    )
    add(
        '抄上游对象并换前缀',
        '抄上游对象并换前缀',
        '抄上游对象并换前缀',
        '抄上游对象并换前缀',
        '抄上游对象并换前缀',
    )
    add(
        '主干：离开的那个接头的 CODE（光交出来的第一段仍抄到达接头）。配线：离开的那个接头/分纤盒的 CODE。仍换光缆前缀。光交本身没有 CODE。',
        '主干：离开的那个接头的 CODE（光交出来的第一段仍抄到达接头）。配线：离开的那个接头/分纤盒的 CODE。仍换光缆前缀。光交本身没有 CODE。',
        '主干：离开的那个接头的 CODE（光交出来的第一段仍抄到达接头）。配线：离开的那个接头/分纤盒的 CODE。仍换光缆前缀。光交本身没有 CODE。',
        '主干：离开的那个接头的 CODE（光交出来的第一段仍抄到达接头）。配线：离开的那个接头/分纤盒的 CODE。仍换光缆前缀。光交本身没有 CODE。',
        '主干：离开的那个接头的 CODE（光交出来的第一段仍抄到达接头）。配线：离开的那个接头/分纤盒的 CODE。仍换光缆前缀。光交本身没有 CODE。',
    )
    add(
        '到达对象原样写入',
        '到达对象原样写入',
        '到达对象原样写入',
        '到达对象原样写入',
        '到达对象原样写入',
    )
    add(
        '主干抄到达接头、配线抄到达分纤盒，CODE 一个字不改（不换光缆前缀）。仍检查城市/PM 是否与主窗口一致。',
        '主干抄到达接头、配线抄到达分纤盒，CODE 一个字不改（不换光缆前缀）。仍检查城市/PM 是否与主窗口一致。',
        '主干抄到达接头、配线抄到达分纤盒，CODE 一个字不改（不换光缆前缀）。仍检查城市/PM 是否与主窗口一致。',
        '主干抄到达接头、配线抄到达分纤盒，CODE 一个字不改（不换光缆前缀）。仍检查城市/PM 是否与主窗口一致。',
        '主干抄到达接头、配线抄到达分纤盒，CODE 一个字不改（不换光缆前缀）。仍检查城市/PM 是否与主窗口一致。',
    )
    add(
        '只取到达对象后三段',
        '只取到达对象后三段',
        '只取到达对象后三段',
        '只取到达对象后三段',
        '只取到达对象后三段',
    )
    add(
        '不管到达对象的前缀和城市/PM，只抄第四/五/六段，再用光缆前缀和主窗口城市/PM 重写。不检查到达对象城市/PM。',
        '不管到达对象的前缀和城市/PM，只抄第四/五/六段，再用光缆前缀和主窗口城市/PM 重写。不检查到达对象城市/PM。',
        '不管到达对象的前缀和城市/PM，只抄第四/五/六段，再用光缆前缀和主窗口城市/PM 重写。不检查到达对象城市/PM。',
        '不管到达对象的前缀和城市/PM，只抄第四/五/六段，再用光缆前缀和主窗口城市/PM 重写。不检查到达对象城市/PM。',
        '不管到达对象的前缀和城市/PM，只抄第四/五/六段，再用光缆前缀和主窗口城市/PM 重写。不检查到达对象城市/PM。',
    )
    add(
        '方案页右侧：模拟预览 + 实际测试（不写入）。不塞进 ntal_engine。',
        '方案页右侧：模拟预览 + 实际测试（不写入）。不塞进 ntal_engine。',
        '方案页右侧：模拟预览 + 实际测试（不写入）。不塞进 ntal_engine。',
        '方案页右侧：模拟预览 + 实际测试（不写入）。不塞进 ntal_engine。',
        '方案页右侧：模拟预览 + 实际测试（不写入）。不塞进 ntal_engine。',
    )
    add(
        '固定示意网：光交O，短干90°→A→B，A 分叉到 C（户数少），长干180°→D。',
        '固定示意网：光交O，短干90°→A→B，A 分叉到 C（户数少），长干180°→D。',
        '固定示意网：光交O，短干90°→A→B，A 分叉到 C（户数少），长干180°→D。',
        '固定示意网：光交O，短干90°→A→B，A 分叉到 C（户数少），长干180°→D。',
        '固定示意网：光交O，短干90°→A→B，A 分叉到 C（户数少），长干180°→D。',
    )
    add(
        '城市',
        '城市',
        '城市',
        '城市',
        '城市',
    )
    add(
        '单盒用户甲（户数 8）',
        '单盒用户甲（户数 8）',
        '单盒用户甲（户数 8）',
        '单盒用户甲（户数 8）',
        '单盒用户甲（户数 8）',
    )
    add(
        '皮线甲',
        '皮线甲',
        '皮线甲',
        '皮线甲',
        '皮线甲',
    )
    add(
        '抄用户户数',
        '抄用户户数',
        '抄用户户数',
        '抄用户户数',
        '抄用户户数',
    )
    add(
        '双盒用户乙（户数 4）',
        '双盒用户乙（户数 4）',
        '双盒用户乙（户数 4）',
        '双盒用户乙（户数 4）',
        '双盒用户乙（户数 4）',
    )
    add(
        '皮线乙1 / 乙2',
        '皮线乙1 / 乙2',
        '皮线乙1 / 乙2',
        '皮线乙1 / 乙2',
        '皮线乙1 / 乙2',
    )
    add(
        '不写',
        '不写',
        '不写',
        '不写',
        '不写',
    )
    add(
        '一个用户接多个盒，该皮线不写',
        '一个用户接多个盒，该皮线不写',
        '一个用户接多个盒，该皮线不写',
        '一个用户接多个盒，该皮线不写',
        '一个用户接多个盒，该皮线不写',
    )
    add(
        '没挂上的皮线',
        '没挂上的皮线',
        '没挂上的皮线',
        '没挂上的皮线',
        '没挂上的皮线',
    )
    add(
        '皮线丙',
        '皮线丙',
        '皮线丙',
        '皮线丙',
        '皮线丙',
    )
    add(
        '保持原值',
        '保持原值',
        '保持原值',
        '保持原值',
        '保持原值',
    )
    add(
        '不改成 0',
        '不改成 0',
        '不改成 0',
        '不改成 0',
        '不改成 0',
    )
    add(
        '盒1 出皮线 8+4',
        '盒1 出皮线 8+4',
        '盒1 出皮线 8+4',
        '盒1 出皮线 8+4',
        '盒1 出皮线 8+4',
    )
    add(
        '分纤盒1',
        '分纤盒1',
        '分纤盒1',
        '分纤盒1',
        '分纤盒1',
    )
    add(
        '所出皮线户数之和',
        '所出皮线户数之和',
        '所出皮线户数之和',
        '所出皮线户数之和',
        '所出皮线户数之和',
    )
    add(
        '用户合计 ≠ 皮线合计',
        '用户合计 ≠ 皮线合计',
        '用户合计 ≠ 皮线合计',
        '用户合计 ≠ 皮线合计',
        '用户合计 ≠ 皮线合计',
    )
    add(
        '整批',
        '整批',
        '整批',
        '整批',
        '整批',
    )
    add(
        '先检查皮线值',
        '先检查皮线值',
        '先检查皮线值',
        '先检查皮线值',
        '先检查皮线值',
    )
    add(
        '没有所出皮线',
        '没有所出皮线',
        '没有所出皮线',
        '没有所出皮线',
        '没有所出皮线',
    )
    add(
        '分纤盒2',
        '分纤盒2',
        '分纤盒2',
        '分纤盒2',
        '分纤盒2',
    )
    add(
        '写 0 允许',
        '写 0 允许',
        '写 0 允许',
        '写 0 允许',
        '写 0 允许',
    )
    add(
        '光交→接头A',
        '光交→接头A',
        '光交→接头A',
        '光交→接头A',
        '光交→接头A',
    )
    add(
        '主干不写户数',
        '主干不写户数',
        '主干不写户数',
        '主干不写户数',
        '主干不写户数',
    )
    add(
        '接头A→盒1→盒2 第一段',
        '接头A→盒1→盒2 第一段',
        '接头A→盒1→盒2 第一段',
        '接头A→盒1→盒2 第一段',
        '接头A→盒1→盒2 第一段',
    )
    add(
        '配线1',
        '配线1',
        '配线1',
        '配线1',
        '配线1',
    )
    add(
        '只写到达的盒1，不加盒2',
        '只写到达的盒1，不加盒2',
        '只写到达的盒1，不加盒2',
        '只写到达的盒1，不加盒2',
        '只写到达的盒1，不加盒2',
    )
    add(
        '盒1→盒2 第二段',
        '盒1→盒2 第二段',
        '盒1→盒2 第二段',
        '盒1→盒2 第二段',
        '盒1→盒2 第二段',
    )
    add(
        '配线2',
        '配线2',
        '配线2',
        '配线2',
        '配线2',
    )
    add(
        '只写到达的盒2',
        '只写到达的盒2',
        '只写到达的盒2',
        '只写到达的盒2',
        '只写到达的盒2',
    )
    add(
        '短干 90° 更短，ODF01',
        '短干 90° 更短，ODF01',
        '短干 90° 更短，ODF01',
        '短干 90° 更短，ODF01',
        '短干 90° 更短，ODF01',
    )
    add(
        '接头A',
        '接头A',
        '接头A',
        '接头A',
        '接头A',
    )
    add(
        '第四段按第一段主干长短，短的号小',
        '第四段按第一段主干长短，短的号小',
        '第四段按第一段主干长短，短的号小',
        '第四段按第一段主干长短，短的号小',
        '第四段按第一段主干长短，短的号小',
    )
    add(
        'A 后主支（户数多）',
        'A 后主支（户数多）',
        'A 后主支（户数多）',
        'A 后主支（户数多）',
        'A 后主支（户数多）',
    )
    add(
        '接头B',
        '接头B',
        '接头B',
        '接头B',
        '接头B',
    )
    add(
        '户数多的接着当前第五段',
        '户数多的接着当前第五段',
        '户数多的接着当前第五段',
        '户数多的接着当前第五段',
        '户数多的接着当前第五段',
    )
    add(
        'A 分叉（户数少）',
        'A 分叉（户数少）',
        'A 分叉（户数少）',
        'A 分叉（户数少）',
        'A 分叉（户数少）',
    )
    add(
        '接头C',
        '接头C',
        '接头C',
        '接头C',
        '接头C',
    )
    add(
        '新开第五段，第六段接最大号后面',
        '新开第五段，第六段接最大号后面',
        '新开第五段，第六段接最大号后面',
        '新开第五段，第六段接最大号后面',
        '新开第五段，第六段接最大号后面',
    )
    add(
        '长干 180°（ODF02）',
        '长干 180°（ODF02）',
        '长干 180°（ODF02）',
        '长干 180°（ODF02）',
        '长干 180°（ODF02）',
    )
    add(
        '接头D',
        '接头D',
        '接头D',
        '接头D',
        '接头D',
    )
    add(
        '另一条出线从 01-01',
        '另一条出线从 01-01',
        '另一条出线从 01-01',
        '另一条出线从 01-01',
        '另一条出线从 01-01',
    )
    add(
        '接头第五段最大 02，户数多的链',
        '接头第五段最大 02，户数多的链',
        '接头第五段最大 02，户数多的链',
        '接头第五段最大 02，户数多的链',
        '接头第五段最大 02，户数多的链',
    )
    add(
        '分纤盒甲',
        '分纤盒甲',
        '分纤盒甲',
        '分纤盒甲',
        '分纤盒甲',
    )
    add(
        '第五段从接头最大 +1 起',
        '第五段从接头最大 +1 起',
        '第五段从接头最大 +1 起',
        '第五段从接头最大 +1 起',
        '第五段从接头最大 +1 起',
    )
    add(
        '同链离接头近的是 01',
        '同链离接头近的是 01',
        '同链离接头近的是 01',
        '同链离接头近的是 01',
        '同链离接头近的是 01',
    )
    add(
        '分纤盒乙',
        '分纤盒乙',
        '分纤盒乙',
        '分纤盒乙',
        '分纤盒乙',
    )
    add(
        '每条链第六段从 01 起',
        '每条链第六段从 01 起',
        '每条链第六段从 01 起',
        '每条链第六段从 01 起',
        '每条链第六段从 01 起',
    )
    add(
        '户数少的另一条配线',
        '户数少的另一条配线',
        '户数少的另一条配线',
        '户数少的另一条配线',
        '户数少的另一条配线',
    )
    add(
        '分纤盒丙',
        '分纤盒丙',
        '分纤盒丙',
        '分纤盒丙',
        '分纤盒丙',
    )
    add(
        '不跟接头共用第五段',
        '不跟接头共用第五段',
        '不跟接头共用第五段',
        '不跟接头共用第五段',
        '不跟接头共用第五段',
    )
    add(
        '抄到达接头，换光缆前缀',
        '抄到达接头，换光缆前缀',
        '抄到达接头，换光缆前缀',
        '抄到达接头，换光缆前缀',
        '抄到达接头，换光缆前缀',
    )
    add(
        '接头A→分纤盒甲',
        '接头A→分纤盒甲',
        '接头A→分纤盒甲',
        '接头A→分纤盒甲',
        '接头A→分纤盒甲',
    )
    add(
        '抄到达分纤盒，换光缆前缀',
        '抄到达分纤盒，换光缆前缀',
        '抄到达分纤盒，换光缆前缀',
        '抄到达分纤盒，换光缆前缀',
        '抄到达分纤盒，换光缆前缀',
    )
    add(
        '不读户数，合格皮线写 1',
        '不读户数，合格皮线写 1',
        '不读户数，合格皮线写 1',
        '不读户数，合格皮线写 1',
        '不读户数，合格皮线写 1',
    )
    add(
        '多盒覆盖仍跳过',
        '多盒覆盖仍跳过',
        '多盒覆盖仍跳过',
        '多盒覆盖仍跳过',
        '多盒覆盖仍跳过',
    )
    add(
        '两端没吸到盒+用户',
        '两端没吸到盒+用户',
        '两端没吸到盒+用户',
        '两端没吸到盒+用户',
        '两端没吸到盒+用户',
    )
    add(
        '皮线乙1',
        '皮线乙1',
        '皮线乙1',
        '皮线乙1',
        '皮线乙1',
    )
    add(
        '多盒也写，各写一遍 4',
        '多盒也写，各写一遍 4',
        '多盒也写，各写一遍 4',
        '多盒也写，各写一遍 4',
        '多盒也写，各写一遍 4',
    )
    add(
        '皮线乙2',
        '皮线乙2',
        '皮线乙2',
        '皮线乙2',
        '皮线乙2',
    )
    add(
        '两条都写，不是对半拆',
        '两条都写，不是对半拆',
        '两条都写，不是对半拆',
        '两条都写，不是对半拆',
        '两条都写，不是对半拆',
    )
    add(
        '同盒重复皮线',
        '同盒重复皮线',
        '同盒重复皮线',
        '同盒重复皮线',
        '同盒重复皮线',
    )
    add(
        '皮线丁',
        '皮线丁',
        '皮线丁',
        '皮线丁',
        '皮线丁',
    )
    add(
        '同一盒到同一用户多于 1 条仍不写',
        '同一盒到同一用户多于 1 条仍不写',
        '同一盒到同一用户多于 1 条仍不写',
        '同一盒到同一用户多于 1 条仍不写',
        '同一盒到同一用户多于 1 条仍不写',
    )
    add(
        '盒1 出 2 条皮线（8+4）',
        '盒1 出 2 条皮线（8+4）',
        '盒1 出 2 条皮线（8+4）',
        '盒1 出 2 条皮线（8+4）',
        '盒1 出 2 条皮线（8+4）',
    )
    add(
        '写条数，不加户数',
        '写条数，不加户数',
        '写条数，不加户数',
        '写条数，不加户数',
        '写条数，不加户数',
    )
    add(
        '仍先核对两个总户数',
        '仍先核对两个总户数',
        '仍先核对两个总户数',
        '仍先核对两个总户数',
        '仍先核对两个总户数',
    )
    add(
        '仍按皮线户数加总',
        '仍按皮线户数加总',
        '仍按皮线户数加总',
        '仍按皮线户数加总',
        '仍按皮线户数加总',
    )
    add(
        '照写，只软错误',
        '照写，只软错误',
        '照写，只软错误',
        '照写，只软错误',
        '照写，只软错误',
    )
    add(
        '对不上不挡写入',
        '对不上不挡写入',
        '对不上不挡写入',
        '对不上不挡写入',
        '对不上不挡写入',
    )
    add(
        '下游盒1(8)+盒2(12) 累加，主干也写',
        '下游盒1(8)+盒2(12) 累加，主干也写',
        '下游盒1(8)+盒2(12) 累加，主干也写',
        '下游盒1(8)+盒2(12) 累加，主干也写',
        '下游盒1(8)+盒2(12) 累加，主干也写',
    )
    add(
        '只到盒2',
        '只到盒2',
        '只到盒2',
        '只到盒2',
        '只到盒2',
    )
    add(
        '配线累加，主干仍空着',
        '配线累加，主干仍空着',
        '配线累加，主干仍空着',
        '配线累加，主干仍空着',
        '配线累加，主干仍空着',
    )
    add(
        '短干 90°（ODF01）',
        '短干 90°（ODF01）',
        '短干 90°（ODF01）',
        '短干 90°（ODF01）',
        '短干 90°（ODF01）',
    )
    add(
        '第一个接头固定 01-01',
        '第一个接头固定 01-01',
        '第一个接头固定 01-01',
        '第一个接头固定 01-01',
        '第一个接头固定 01-01',
    )
    add(
        '第五段一直 01',
        '第五段一直 01',
        '第五段一直 01',
        '第五段一直 01',
        '第五段一直 01',
    )
    add(
        '分叉也接着编，不新开第五段',
        '分叉也接着编，不新开第五段',
        '分叉也接着编，不新开第五段',
        '分叉也接着编，不新开第五段',
        '分叉也接着编，不新开第五段',
    )
    add(
        '另一条出线自己的第四段',
        '另一条出线自己的第四段',
        '另一条出线自己的第四段',
        '另一条出线自己的第四段',
        '另一条出线自己的第四段',
    )
    add(
        '第一个 01-01',
        '第一个 01-01',
        '第一个 01-01',
        '第一个 01-01',
        '第一个 01-01',
    )
    add(
        '每到一个接头新开第五段',
        '每到一个接头新开第五段',
        '每到一个接头新开第五段',
        '每到一个接头新开第五段',
        '每到一个接头新开第五段',
    )
    add(
        '第六段固定 01',
        '第六段固定 01',
        '第六段固定 01',
        '第六段固定 01',
        '第六段固定 01',
    )
    add(
        '长干 180° 更接近起始角 100°',
        '长干 180° 更接近起始角 100°',
        '长干 180° 更接近起始角 100°',
        '长干 180° 更接近起始角 100°',
        '长干 180° 更接近起始角 100°',
    )
    add(
        '第四段先比出线角度',
        '第四段先比出线角度',
        '第四段先比出线角度',
        '第四段先比出线角度',
        '第四段先比出线角度',
    )
    add(
        '短干 90° 排第二',
        '短干 90° 排第二',
        '短干 90° 排第二',
        '短干 90° 排第二',
        '短干 90° 排第二',
    )
    add(
        '角度定完再比主干长短',
        '角度定完再比主干长短',
        '角度定完再比主干长短',
        '角度定完再比主干长短',
        '角度定完再比主干长短',
    )
    add(
        '后两段仍按分叉另开第五段',
        '后两段仍按分叉另开第五段',
        '后两段仍按分叉另开第五段',
        '后两段仍按分叉另开第五段',
        '后两段仍按分叉另开第五段',
    )
    add(
        '户数少的新开第五段',
        '户数少的新开第五段',
        '户数少的新开第五段',
        '户数少的新开第五段',
        '户数少的新开第五段',
    )
    add(
        '接头A 是 01-01，下挂盒甲（户数多）',
        '接头A 是 01-01，下挂盒甲（户数多）',
        '接头A 是 01-01，下挂盒甲（户数多）',
        '接头A 是 01-01，下挂盒甲（户数多）',
        '接头A 是 01-01，下挂盒甲（户数多）',
    )
    add(
        '第五段跟所接接头相同',
        '第五段跟所接接头相同',
        '第五段跟所接接头相同',
        '第五段跟所接接头相同',
        '第五段跟所接接头相同',
    )
    add(
        '同一接头下另一条配线 盒乙',
        '同一接头下另一条配线 盒乙',
        '同一接头下另一条配线 盒乙',
        '同一接头下另一条配线 盒乙',
        '同一接头下另一条配线 盒乙',
    )
    add(
        '第六段接着编，不每条链从 01 起',
        '第六段接着编，不每条链从 01 起',
        '第六段接着编，不每条链从 01 起',
        '第六段接着编，不每条链从 01 起',
        '第六段接着编，不每条链从 01 起',
    )
    add(
        '接头A 下 盒甲（户数多）',
        '接头A 下 盒甲（户数多）',
        '接头A 下 盒甲（户数多）',
        '接头A 下 盒甲（户数多）',
        '接头A 下 盒甲（户数多）',
    )
    add(
        '每个接头自己的配线从 01 起',
        '每个接头自己的配线从 01 起',
        '每个接头自己的配线从 01 起',
        '每个接头自己的配线从 01 起',
        '每个接头自己的配线从 01 起',
    )
    add(
        '接头B 下 盒丙',
        '接头B 下 盒丙',
        '接头B 下 盒丙',
        '接头B 下 盒丙',
        '接头B 下 盒丙',
    )
    add(
        '不看同 ODF 其它接头用到几',
        '不看同 ODF 其它接头用到几',
        '不看同 ODF 其它接头用到几',
        '不看同 ODF 其它接头用到几',
        '不看同 ODF 其它接头用到几',
    )
    add(
        '第五段从 03 起',
        '第五段从 03 起',
        '第五段从 03 起',
        '第五段从 03 起',
        '第五段从 03 起',
    )
    add(
        '同链第二个盒',
        '同链第二个盒',
        '同链第二个盒',
        '同链第二个盒',
        '同链第二个盒',
    )
    add(
        '同链接着 02',
        '同链接着 02',
        '同链接着 02',
        '同链接着 02',
        '同链接着 02',
    )
    add(
        '下一条配线',
        '下一条配线',
        '下一条配线',
        '下一条配线',
        '下一条配线',
    )
    add(
        '第六段整条 ODF 连续，不按链归零',
        '第六段整条 ODF 连续，不按链归零',
        '第六段整条 ODF 连续，不按链归零',
        '第六段整条 ODF 连续，不按链归零',
        '第六段整条 ODF 连续，不按链归零',
    )
    add(
        '光交没有 CODE，第一段仍抄到达接头',
        '光交没有 CODE，第一段仍抄到达接头',
        '光交没有 CODE，第一段仍抄到达接头',
        '光交没有 CODE，第一段仍抄到达接头',
        '光交没有 CODE，第一段仍抄到达接头',
    )
    add(
        '接头A→接头B',
        '接头A→接头B',
        '接头A→接头B',
        '接头A→接头B',
        '接头A→接头B',
    )
    add(
        '抄离开的接头A，不是到达的 B',
        '抄离开的接头A，不是到达的 B',
        '抄离开的接头A，不是到达的 B',
        '抄离开的接头A，不是到达的 B',
        '抄离开的接头A，不是到达的 B',
    )
    add(
        '抄离开的接头A',
        '抄离开的接头A',
        '抄离开的接头A',
        '抄离开的接头A',
        '抄离开的接头A',
    )
    add(
        '到达接头 CODE 原样写入，不换光缆前缀',
        '到达接头 CODE 原样写入，不换光缆前缀',
        '到达接头 CODE 原样写入，不换光缆前缀',
        '到达接头 CODE 原样写入，不换光缆前缀',
        '到达接头 CODE 原样写入，不换光缆前缀',
    )
    add(
        '到达分纤盒 CODE 原样写入',
        '到达分纤盒 CODE 原样写入',
        '到达分纤盒 CODE 原样写入',
        '到达分纤盒 CODE 原样写入',
        '到达分纤盒 CODE 原样写入',
    )
    add(
        '到达接头后三段 01-01-01',
        '到达接头后三段 01-01-01',
        '到达接头后三段 01-01-01',
        '到达接头后三段 01-01-01',
        '到达接头后三段 01-01-01',
    )
    add(
        '只抄后三段，前缀/城市/PM 用光缆和主窗口',
        '只抄后三段，前缀/城市/PM 用光缆和主窗口',
        '只抄后三段，前缀/城市/PM 用光缆和主窗口',
        '只抄后三段，前缀/城市/PM 用光缆和主窗口',
        '只抄后三段，前缀/城市/PM 用光缆和主窗口',
    )
    add(
        '到达盒后三段 01-03-01',
        '到达盒后三段 01-03-01',
        '到达盒后三段 01-03-01',
        '到达盒后三段 01-03-01',
        '到达盒后三段 01-03-01',
    )
    add(
        '不检查到达对象自己的城市/PM',
        '不检查到达对象自己的城市/PM',
        '不检查到达对象自己的城市/PM',
        '不检查到达对象自己的城市/PM',
        '不检查到达对象自己的城市/PM',
    )
    add(
        '场景',
        'Caso',
        'Caso',
        'Cas',
        'حالة',
    )
    add(
        '对象',
        'Objeto',
        'Objeto',
        'Objet',
        'عنصر',
    )
    add(
        '将写成',
        'Se escribirá',
        'Se escribirá',
        'Sera écrit',
        'سيُكتب',
    )
    add(
        '原值',
        'Valor actual',
        'Valor actual',
        'Valeur actuelle',
        'القيمة الحالية',
    )
    add(
        '备注',
        'Nota',
        'Nota',
        'Remarque',
        'ملاحظة',
    )
    add(
        '把上面数字调大',
        '把上面数字调大',
        '把上面数字调大',
        '把上面数字调大',
        '把上面数字调大',
    )
    add(
        '（没有将写入的要素）',
        '（没有将写入的要素）',
        '（没有将写入的要素）',
        '（没有将写入的要素）',
        '（没有将写入的要素）',
    )
    add(
        '本功能方案：{}。将写入 {} {}，硬错误 {}，软错误 {}，警告 {}。没有写入，也没有出临时图层。',
        '本功能方案：{}。将写入 {} {}，硬错误 {}，软错误 {}，警告 {}。没有写入，也没有出临时图层。',
        '本功能方案：{}。将写入 {} {}，硬错误 {}，软错误 {}，警告 {}。没有写入，也没有出临时图层。',
        '本功能方案：{}。将写入 {} {}，硬错误 {}，软错误 {}，警告 {}。没有写入，也没有出临时图层。',
        '本功能方案：{}。将写入 {} {}，硬错误 {}，软错误 {}，警告 {}。没有写入，也没有出临时图层。',
    )
    add(
        '按本窗当前容差 / 角度 / 六个方案检测。硬错误 {}，软错误 {}，警告 {}。没有写入，没有翻转，没有出图层。',
        '按本窗当前容差 / 角度 / 六个方案检测。硬错误 {}，软错误 {}，警告 {}。没有写入，没有翻转，没有出图层。',
        '按本窗当前容差 / 角度 / 六个方案检测。硬错误 {}，软错误 {}，警告 {}。没有写入，没有翻转，没有出图层。',
        '按本窗当前容差 / 角度 / 六个方案检测。硬错误 {}，软错误 {}，警告 {}。没有写入，没有翻转，没有出图层。',
        '按本窗当前容差 / 角度 / 六个方案检测。硬错误 {}，软错误 {}，警告 {}。没有写入，没有翻转，没有出图层。',
    )
    add(
        '配置',
        '配置',
        '配置',
        '配置',
        '配置',
    )
    add(
        '测试没跑成：{}',
        '测试没跑成：{}',
        '测试没跑成：{}',
        '测试没跑成：{}',
        '测试没跑成：{}',
    )
    add(
        '全面检测没跑成：{}',
        '全面检测没跑成：{}',
        '全面检测没跑成：{}',
        '全面检测没跑成：{}',
        '全面检测没跑成：{}',
    )
    add(
        '……还有 {} 条',
        '……还有 {} 条',
        '……还有 {} 条',
        '……还有 {} 条',
        '……还有 {} 条',
    )
    return rows


_ROWS = _rows()
EN = {item[0]: item[1] for item in _ROWS}
ES = {item[0]: item[2] for item in _ROWS}
FR = {item[0]: item[3] for item in _ROWS}
AR = {item[0]: item[4] for item in _ROWS}

