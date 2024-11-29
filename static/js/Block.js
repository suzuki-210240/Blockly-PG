//-------------Blockly設定用javascript------------------

//---Blockly のワークスペースを設定---
var workspace = Blockly.inject('blocklyDiv', {
    toolbox: `
    <xml xmlns="https://developers.google.com/blockly/xml">
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

        <!-- 型を指定できる変数 カテゴリ -->
        <category name="変数（型指定）" colour="265" custom="VARIABLE_DYNAMIC"></category>

        <!-- リスト操作 カテゴリ -->
        <category name="リスト操作" colour="260">
            <block type="lists_create_with"></block>
            <block type="lists_length"></block>
            <block type="lists_getIndex"></block>
            <block type="lists_setIndex"></block>
            <block type="lists_insert"></block>
        </category>

        <!-- 関数 カテゴリ -->
        <category name="関数" colour="270" custom="PROCEDURE"></category>


    </xml>
    `
});

//---lists_insertのカスタム設定定義---
Blockly.defineBlocksWithJsonArray([{
  "type": "lists_insert",
  "message0": "insert %1 at index %2 in list %3",
  "args0": [
    {
      "type": "input_value",
      "name": "VALUE"
    },
    {
      "type": "input_value",
      "name": "INDEX"
    },
    {
      "type": "input_value",
      "name": "LIST"
    }
  ],
  "colour": 260,
  "tooltip": "Insert an item at a specific index in a list.",
  "helpUrl": ""
}]);