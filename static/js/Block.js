// Blockly のワークスペースを設定
var workspace = Blockly.inject('blocklyDiv', {
    toolbox: `
    <xml xmlns="https://developers.google.com/blockly/xml">
        </category>
        <!-- コントローラ カテゴリ -->
        <category name="コントローラ" colour="210">
            <block type="controls_if"></block>
            <block type="controls_whileUntil"></block>
            <block type="controls_for"></block>
        </category>
        <!-- ループ カテゴリ -->
        <category name="ループ" colour="120">
            <block type="controls_repeat_ext"></block>
        </category>

        <!-- ロジック カテゴリ -->
        <category name="ロジック" colour="210">
            <block type="logic_compare"></block>
            <block type="logic_operation"></block>
            <block type="logic_boolean"></block>
        </category>

        <!-- テキスト カテゴリ -->
        <category name="テキスト" colour="220">
            <block type="text"></block>
            <block type="text_print"></block>
        </category>

        <!-- 計算 カテゴリ -->
        <category name="計算" colour="230">
            <block type="math_number"></block>
            <block type="math_arithmetic"></block>
            <block type="math_round"></block>
        </category>
        <!-- 変数 カテゴリ -->
        <category name="変数" colour="330" custom="VARIABLE"></category>
        <!-- リスト操作カテゴリ -->
        <category name="リスト操作" colour="260">
          <block type="list_create_empty"></block>
          <block type="list_create_with"></block>
          <block type="list_length"></block>
          <block type="list_append"></block>
        </category>


    </xml>
    `
});