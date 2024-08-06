import os
import random
from PIL import Image, ImageDraw, ImageFont
from config import get_settings
from loguru import logger
import matplotlib.font_manager

class ImageService:
    def __init__(self):
        self.settings = get_settings()
        self.font_cache = {}
    
    def get_random_background(self):
        logger.info("ランダムな背景画像を選択中...")
        background_dir = os.path.join(self.settings.RELEASE_NOTES_DIR, 'assets')
        background_images = [f for f in os.listdir(background_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]
        if not background_images:
            logger.error("背景画像が見つかりません。")
            raise FileNotFoundError("No background images found in the assets directory.")
        selected_image = random.choice(background_images)
        logger.success(f"背景画像 '{selected_image}' を選択しました。")
        return os.path.join(background_dir, selected_image)
    
    def list_available_fonts(self):
        logger.info("使用可能なフォントの一覧を表示します...")
        
        # システムフォントの一覧
        system_fonts = set(f.name for f in matplotlib.font_manager.fontManager.ttflist)
        logger.info("システムフォント:")
        for font in sorted(system_fonts):
            logger.info(f"  - {font}")
        
        # カスタムフォント
        custom_font_dir = os.path.join(self.settings.RELEASE_NOTES_DIR, 'assets')
        custom_fonts = [f for f in os.listdir(custom_font_dir) if f.endswith('.ttf')]
        if custom_fonts:
            logger.info("カスタムフォント:")
            for font in custom_fonts:
                logger.info(f"  - {font}")
        else:
            logger.info("カスタムフォントは見つかりませんでした。")
    
    def get_font(self, font_name, font_size):
        logger.info(f"フォント '{font_name}' (サイズ: {font_size}) を読み込み中...")
        
        if (font_name, font_size) in self.font_cache:
            return self.font_cache[(font_name, font_size)]
        
        # 指定されたフォントファイルを探す
        if os.path.exists(font_name):
            try:
                font = ImageFont.truetype(font_name, font_size)
                logger.success(f"指定されたフォントファイル '{font_name}' を読み込みました。")
                self.font_cache[(font_name, font_size)] = font
                return font
            except OSError:
                logger.warning(f"指定されたフォントファイル '{font_name}' の読み込みに失敗しました。")
        
        # assets ディレクトリ内でフォントを探す
        font_extensions = ['.otf', '.ttf']
        for ext in font_extensions:
            custom_font_path = os.path.join(self.settings.RELEASE_NOTES_DIR, 'assets', font_name + ext)
            if os.path.exists(custom_font_path):
                try:
                    font = ImageFont.truetype(custom_font_path, font_size)
                    logger.success(f"カスタムフォント '{custom_font_path}' を読み込みました。")
                    self.font_cache[(font_name, font_size)] = font
                    return font
                except OSError:
                    logger.warning(f"カスタムフォント '{custom_font_path}' の読み込みに失敗しました。")
        
        # システムフォントを探す
        try:
            font_path = matplotlib.font_manager.findfont(matplotlib.font_manager.FontProperties(family=font_name))
            font = ImageFont.truetype(font_path, font_size)
            logger.success(f"システムフォント '{font_name}' を読み込みました。")
            self.font_cache[(font_name, font_size)] = font
            return font
        except OSError:
            logger.warning(f"システムフォント '{font_name}' の読み込みに失敗しました。")
        
        # フォールバック: デフォルトフォント
        logger.warning(f"フォント '{font_name}' が見つかりませんでした。デフォルトフォントを使用します。")
        default_font = ImageFont.load_default().font_variant(size=font_size)
        self.font_cache[(font_name, font_size)] = default_font
        return default_font
    
    def calculate_font_size(self, img_width, img_height, text, font_name):
        target_width = img_width * 0.5
        font_size = 10
        font = self.get_font(font_name, font_size)
        bbox = font.getbbox(text)
        text_width = bbox[2] - bbox[0]
        
        while text_width < target_width:
            font_size += 5
            font = self.get_font(font_name, font_size)
            bbox = font.getbbox(text)
            text_width = bbox[2] - bbox[0]
        
        return font_size - 5

    def generate_header_image(self, tag: str, output_path: str, font_name: str = "Times New Roman"):
        self.list_available_fonts()
        
        logger.info(f"ヘッダー画像の生成を開始: タグ '{tag}', フォント '{font_name}'")
        background_path = self.get_random_background()
        
        logger.info("背景画像を開いています...")
        img = Image.open(background_path)
        draw = ImageDraw.Draw(img)
        
        font_size = self.calculate_font_size(img.width, img.height, tag, font_name)
        logger.info(f"計算されたフォントサイズ: {font_size}")
        font = self.get_font(font_name, font_size)
        
        logger.info("テキストのサイズと位置を計算中...")
        bbox = font.getbbox(tag)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        # テキストを画像の中央に配置
        position = ((img.width - text_width) / 2, (img.height - text_height) / 2)
        
        logger.info("画像にテキストを描画中...")
        draw.text(position, tag, font=font, fill=(255, 255, 255))
        
        logger.info(f"画像を保存中: {output_path}")
        img.save(output_path)
        logger.success(f"ヘッダー画像が正常に生成されました: {output_path}")
