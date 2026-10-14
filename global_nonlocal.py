# global と nonlocal の使い分け

# ========================================
# 1. global: グローバル変数を参照・変更する
# ========================================
x = 10  # グローバル変数

def modify_global():
    """グローバル変数を変更する場合はglobalを使う"""
    global x
    x = 20
    print(f"modify_global内: x = {x}")

print("--- global の例 ---")
print(f"修正前: x = {x}")
modify_global()
print(f"修正後: x = {x}")  # グローバル変数が変更される


# ========================================
# 2. nonlocal: 外側の関数のローカル変数を参照・変更する
# ========================================
def outer():
    """外側の関数"""
    y = 10  # outer関数のローカル変数
    
    def inner():
        """内側の関数"""
        nonlocal y  # 外側関数のyを参照・変更する
        y = 20
        print(f"inner内: y = {y}")
    
    print(f"修正前: y = {y}")
    inner()
    print(f"修正後: y = {y}")  # outer関数のyが変更される

print("\n--- nonlocal の例 ---")
outer()


# ========================================
# 3. 違いを比較する例
# ========================================
global_var = 100
print("\n--- global と nonlocal の比較 ---")
print(f"global_var (グローバル) = {global_var}")

def outer_func():
    """外側の関数"""
    local_var = 100  # 外側関数のローカル変数
    
    def inner_func():
        """内側の関数"""
        global global_var  # グローバル変数を参照
        nonlocal local_var  # 外側関数のローカル変数を参照
        
        global_var += 10  # グローバル変数を変更
        local_var += 10   # 外側関数のローカル変数を変更
        
        print(f"inner_func内: global_var = {global_var}, local_var = {local_var}")
    
    print(f"修正前: local_var = {local_var}")
    inner_func()
    print(f"修正後: local_var = {local_var}")

outer_func()
print(f"修正後: global_var = {global_var}")


# ========================================
# 4. 何も指定しない場合の注意
# ========================================
print("\n--- global/nonlocal がない場合 ---")

a = 50

def wrong_try():
    """globalなしでグローバル変数を変更しようとする"""
    try:
        a += 1  # エラー: ローカル変数として扱われるが、値が定義されていない
    except UnboundLocalError as e:
        print(f"エラー: {e}")

wrong_try()

# 正しい方法
def correct_try():
    """globalを使ってグローバル変数を変更する"""
    global a
    a += 1
    print(f"修正後: a = {a}")

correct_try()


# ========================================
# 5. ネストされた関数の複数層の場合
# ========================================
print("\n--- ネストされた複数層の関数 ---")

def level1():
    """第1層"""
    value = 1
    
    def level2():
        """第2層"""
        nonlocal value
        value = 2
        
        def level3():
            """第3層"""
            nonlocal value
            value = 3
            print(f"level3内: value = {value}")
        
        level3()
        print(f"level2内: value = {value}")
    
    level2()
    print(f"level1内: value = {value}")

level1()


# ========================================
# まとめ
# ========================================
print("\n" + "="*50)
print("【使い分けまとめ】")
print("="*50)
print("global: スクリプト全体で共通の変数を参照・変更したい時")
print("nonlocal: 外側の関数(親関数)のローカル変数を参照・変更したい時")
print("何も指定しない: 新しいローカル変数を作成（スコープは関数内）")
