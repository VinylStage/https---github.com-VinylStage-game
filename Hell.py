import random


# 캐릭터기본스탯
class Character:
    def __init__(self, name, HP, MP, ENG, BLF, ATK, INT, FTH, DEF, REP, AGI, VIT, REM, RST):
        self.name = name

        # 소모용
        self.HP = HP  # 체력
        self.MP = MP  # 마나
        self.ENG = ENG  # 기력
        self.BLF = BLF  # 믿음/Holy Knight의 마나역할

        # 고정스탯
        self.ATK = ATK  # 공격력
        self.INT = INT  # 지능/주문력
        self.FTH = FTH  # 신앙력
        self.DEF = DEF  # 방어력
        self.REP = REP  # 마법저항력
        self.AGI = AGI  # 민첩/회피율
        self.VIT = VIT  # 체력재생력
        self.RST = RST  # 기력재생력
        self.REM = REM  # 마나재생력

# 소드마스터
        # 소마 평타

    def swordman_attack(self, target):
        if random.random() < self.AGI:
            return
        damage = self.ATK + random.randint(-50, 100)  # 랜덤으로 치명타 적용
        damage -= target.DEF  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 오소이')
        target.HP -= damage
        print(f'{target.name}에게 {damage}만큼 칼로 찔렀다.')
        self.HP += self.VIT
        print(f'{self.name}은(는) {self.VIT}만큼 체력을 회복했다.')
        if target.HP <= 0:
            print(f'{target.name}녀석 {damage}맞고 죽음')
            self.HP += self.VIT*1.5
            print(f'{self.name}은(는) {self.VIT*1.5}만큼 체력을 회복했다.')
            print('================================================================================================')

    # 소용돌이

    def whirlwind(self, target):
        if random.random() < target.AGI:
            return
        damage = self.ATK*0.8
        damage -= target.DEF
        if damage < 0:
            damage = 0
            print(f'{target.name} : 오소이')
        target.HP -= damage
        print(f'{target.name}은 {damage}만큼 망가졌다!')
        self.HP += self.VIT
        print(f'{self.name}은(는) {self.VIT}만큼 체력을 회복했다.')
        if target.HP <= 0:
            print(f'{target.name}, 소용돌이로 가루가 되었다.')
            self.HP += self.VIT*1.5
            print(f'{self.name}은(는) {self.VIT*1.5}만큼 체력을 회복했다.')
            print('================================================================================================')

    # 머리찢기
    def tearoffhead(self, target):
        if random.random() < target.AGI:
            return
        damage = self.ATK*1.2
        damage -= target.DEF
        if damage < 0:
            damage = 0
            print(f'{target.name} : 오소이')
        target.HP -= damage
        print(f'{target.name}에게 {damage}만큼 머리가 찢어졌다!')
        self.HP += self.VIT
        print(f'{self.name}은(는) {self.VIT}만큼 체력을 회복했다.')
        if target.HP <= 0:
            print(f'{target.name}의 머리가 사라졌다!')
            self.HP += self.VIT*1.5
            print(f'{self.name}은(는) {self.VIT*1.5}만큼 체력을 회복했다.')
            print('================================================================================================')

    # 기합
    def spirited(self, target):
        target.DEF -= 20
        self.DEF += 30
        self.HP += 50
        self.HP += self.VIT
        print(f'{self.name}은(는) {self.VIT}만큼 체력을 회복했다.')
        print(f'{target.name}은(는) 겁에질려 방어력이 20 떨어지고',
              f'{self.name}은(는) 방어력이 30 오르고 50 체력을 회복했다!', sep='\n')
        if target.DEF <= 0:
            print(f'{target.name}이(가) 겁에질려 그대로 쓰러졌다!')
            self.HP += self.VIT*1.5
            print(f'{self.name}은(는) {self.VIT*1.5}만큼 체력을 회복했다.')
            print('================================================================================================')

# 성기사
        # 성기사 평타
    def holy_attack(self, target):
        if random.random() < target.AGI:
            return
        damage = self.ATK + self.FTH*0.2 + \
            random.randint(-20, 150)  # 랜덤으로 치명타 적용
        damage -= target.DEF  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 오소이')
        target.HP -= damage
        print(f'{target.name}에게 {damage}만큼 입혔다!')
        self.HP += self.VIT
        print(f'{self.name}은(는) {self.VIT}만큼 체력을 회복했다.')
        if target.HP <= 0:
            print(f'{target.name}이 성스러워졌다!')
            self.HP += self.VIT*1.5
            print(f'{self.name}은(는) {self.VIT*1.5}만큼 체력을 회복했다.')
            print('================================================================================================')

        # 신성한불꽃
    def sacredfire(self, target):
        if random.random() < target.AGI:
            return
        damage = self.FTH*0.7
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 오소이')
        target.HP -= damage
        print(f'대충{target.name}에게 {damage}만큼 뜨끈뜨끈해졌다!')
        self.BLF -= 10
        print(f'스킬사용으로 믿음이 10 소모 : {self.BLF}')
        self.HP += self.VIT
        print(f'{self.name}은(는) {self.VIT}만큼 체력을 회복했다.')
        if target.HP <= 0:
            print(f'{target.name}, 귀중한 단백질원이 되었다')
            self.BLF -= 10
            print(f'스킬사용으로 믿음이 10 소모 : {self.BLF}')
            self.HP += self.VIT*1.5
            print(f'{self.name}은(는) {self.VIT*1.5}만큼 체력을 회복했다.')
            print('================================================================================================')

        # 신성한 빛줄기
    def holyvolt(self, target):
        if random.random() < target.AGI:
            return
        damage = self.FTH
        damage -= target.DEF  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 오소이')
        target.HP -= damage
        print(f'{target.name}에게 {damage}빛을 보게했다!')
        self.BLF -= 30
        print(f'스킬사용으로 믿음이 10 소모 : {self.BLF}')
        self.HP += self.VIT
        print(f'{self.name}은(는) {self.VIT}만큼 체력을 회복했다.')
        if target.HP <= 0:
            print(f'{target.name}아 제발 밖에좀 나가서', '\n', '햇빛도 좀 보고 잔디도 만지고 좀 그래!')
            self.HP += self.VIT*1.5
            print(f'{self.name}은(는) {self.VIT*1.5}만큼 체력을 회복했다.')
            print('================================================================================================')

        # 기도
    def pray(self, target):
        effect = self.HP + self.FTH*0.3
        self.HP += effect
        self.BLF += effect*0.5
        print(f'체력을 {effect}만큼 회복하고 믿음을 {effect*0.5}만큼 회복했다!')
        self.HP += self.VIT
        print(f'{self.name}은(는) {self.VIT}만큼 체력을 회복했다.')
        print('================================================================================================')

# 원소술사
        # 원소술사 평타
    def sorceress_attack(self, target):
        if random.random() < target.AGI:
            return
        damage = self.ATK + self.INT*0.1 + \
            random.randint(-50, 20)  # 랜덤으로 치명타 적용
        damage -= target.DEF  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 오소이')
        target.HP -= damage
        print(f'대충{target.name}에게 {damage}만큼 톡!')
        self.HP += self.VIT
        print(f'{self.name}은(는) {self.VIT}만큼 체력을 회복했다.')
        self.MP += self.REM
        print(f'{self.name}은(는) {self.REM}만큼 마나를 회복했다.',
              f'현재마나 : {self.MP}', sep='\n')
        if target.HP <= 0:
            print('너는 뭘해도 죽을놈이구나')
            self.HP += self.VIT*1.5
            print(f'{self.name}은(는) {self.VIT*1.5}만큼 체력을 회복했다.')
            self.MP += self.REM*1.5
            print(f'{self.name}은(는) {self.REM*1.5}만큼 마나를 회복했다.',
                  f'현재마나 : {self.MP}', sep='\n')
            print('================================================================================================')

        # 구멍속불
    def fireinthehole(self, target):
        if random.random() < target.AGI:
            return
        damage = self.INT*0.6
        damage -= target.REP  # 방어력으로 물리공격 상쇄
        self.MP -= 20
        print('20마나 사용')
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 오소이')
        target.HP -= damage
        print(f'{target.name}자식 {damage}만큼 익었다!')
        self.HP += self.VIT
        print(f'{self.name}은(는) {self.VIT}만큼 체력을 회복했다.')
        self.MP += self.REM
        print(f'{self.name}은(는) {self.REM}만큼 마나를 회복했다.',
              f'현재마나 : {self.MP}', sep='\n')
        if target.HP <= 0:
            print(f'{target.name}, 맛있는 냄새가 솔솔 피어오른다.')
            self.MP -= 20
            print(f'20마나 사용 : {self.MP}')
            self.HP += self.VIT*1.5
            print(f'{self.name}은(는) {self.VIT*1.5}만큼 체력을 회복했다.')
            self.MP += self.REM
            print(f'{self.name}은(는) {self.REM*1.5}만큼 마나를 회복했다.',
                  f'현재마나 : {self.MP}', sep='\n')
            print('================================================================================================')

        # 얼음숨결
    def icebreath(self, target):
        if random.random() < target.AGI:
            return
        damage = self.INT*0.5
        damage -= target.REP  # 방어력으로 물리공격 상쇄
        self.MP -= 25
        print('25마나 사용')
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 오소이')
        target.HP -= damage
        print(f'{target.name}놈 얼리고 {damage}를 입었다!')
        self.HP += self.VIT
        print(f'{self.name}은(는) {self.VIT}만큼 체력을 회복했다.')
        self.MP += self.REM
        print(f'{self.name}은(는) {self.REM}만큼 마나를 회복했다.',
              f'현재마나 : {self.MP}', sep='\n')
        if target.HP <= 0:
            print(f'{target.name}, 선채로 사망..!')
            self.MP -= 25
            print(f'25마나 사용 : {self.MP}')
            self.HP += self.VIT*1.5
            print(f'{self.name}은(는) {self.VIT*1.5}만큼 체력을 회복했다.')
            self.MP += self.REM
            print(f'{self.name}은(는) {self.REM*1.5}만큼 마나를 회복했다.',
                  f'현재마나 : {self.MP}', sep='\n')
            print('================================================================================================')

        # 묻어버리기
    def dirtgrave(self, target):
        if random.random() < target.AGI:
            return
        damage = self.INT*0.8
        damage -= target.DEF  # 방어력으로 물리공격 상쇄
        self.MP -= 30
        print('30마나 사용')
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 오소이')
        target.HP -= damage
        print(f'{target.name}녀석 {damage}피해를 입고 겨우 흙더미에서 나왔다')
        self.HP += self.VIT
        print(f'{self.name}은(는) {self.VIT}만큼 체력을 회복했다.')
        self.MP += self.REM
        print(f'{self.name}은(는) {self.REM}만큼 마나를 회복했다.',
              f'현재마나 : {self.MP}', sep='\n')
        if target.HP <= 0:
            print(f'{target.name}, 생 매 장 ~')
            self.MP -= 30
            print(f'30마나 사용 : {self.MP}')
            self.HP += self.VIT*1.5
            print(f'{self.name}은(는) {self.VIT*1.5}만큼 체력을 회복했다.')
            self.MP += self.REM
            print(f'{self.name}은(는) {self.REM*1.5}만큼 마나를 회복했다.',
                  f'현재마나 : {self.MP}', sep='\n')
            print('================================================================================================')

        # 회복
    def healself(self, target):
        self.HP += self.INT*0.3
        print(f'내 체력이 {self.INT*0.3}만큼 회복되었다.')
        self.MP -= 50
        print('50마나 사용')
        self.HP += self.VIT
        print(f'{self.name}은(는) {self.VIT}만큼 체력을 회복했다.')
        self.MP += self.REM
        print(f'{self.name}은(는) {self.REM}만큼 마나를 회복했다.',
              f'현재마나 : {self.MP}', sep='\n')
        print('================================================================================================')

# 인파이터
        # 인파 평타
    def infighter_attack(self, target):
        if random.random() < target.AGI:
            return
        damage = self.ATK + random.randint(-50, 200)  # 랜덤으로 치명타 적용
        damage -= target.DEF  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 오소이')
        target.HP -= damage
        print(f'{damage} 톡!')
        self.HP += self.VIT
        print(f'{self.name}은(는) {self.VIT}만큼 체력을 회복했다.')
        self.ENG += self.RST
        print(f'{self.name}은(는) {self.RST}만큼 기력을 회복했다.',
              f'현재 기력: {self.ENG}', sep='\n')
        if target.HP <= 0:
            print(f'톡 쳤더니 죽어버린 {target.name} 코이츠 wwwww')
            self.HP += self.VIT*1.5
            print(f'{self.name}은(는) {self.VIT*1.5}만큼 체력을 회복했다.')
            self.ENG += self.RST*1.5
            print(f'{self.name}은(는) {self.RST*1.5}만큼 기력을 회복했다.',
                  f'현재 기력: {self.ENG}', sep='\n')
            print('================================================================================================')

        # 진심펀치
    def sincerepunch(self, target):
        if random.random() < target.AGI:
            return
        damage = self.ATK*0.7
        damage -= target.DEF  # 방어력으로 물리공격 상쇄
        target.DEF = target.DEF - self.ATK*0.3
        self.ENG -= 50
        print('50 기력사용')
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 오소이')
        target.HP -= damage
        print(f'{damage}만큼 맞고 {self.ATK*0.3}만큼 방어력을 깎았다!')
        self.HP += self.VIT
        print(f'{self.name}은(는) {self.VIT}만큼 체력을 회복했다.')
        self.ENG += self.RST
        print(f'{self.name}은(는) {self.RST}만큼 기력을 회복했다.',
              f'현재 기력: {self.ENG}', sep='\n')
        if target.DEF <= 0:
            target.HP -= 10000
            print(f'{target.name}녀석 방어구가 부서지고 쓰러졌어!')
            self.ENG += self.RST*1.5
            print(f'{self.name}은(는) {self.RST*1.5}만큼 기력을 회복했다.',
                  f'현재 기력: {self.ENG}')
            print('================================================================================================')
        elif target.HP <= 0:
            print(f'{target.name}, DOWN! {target.name}, DOWN!')
            self.HP += self.VIT*1.5
            print(f'{self.name}은(는) {self.VIT*1.5}만큼 체력을 회복했다.')
            self.ENG += self.RST*1.5
            print(f'{self.name}은(는) {self.RST*1.5}만큼 기력을 회복했다.',
                  f'현재 기력: {self.ENG}', sep='\n')
            print('================================================================================================')

        # 회전차기
    def whirlkick(self, target):
        if random.random() < target.AGI:
            return
        damage = self.ATK*1.2
        damage -= target.DEF  # 방어력으로 물리공격 상쇄
        self.ENG -= 30
        print('30 기력사용')
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 오소이')
        target.HP -= damage
        print(f'{damage}만큼 아픈 주먹!')
        self.HP += self.VIT
        print(f'{self.name}은(는) {self.VIT}만큼 체력을 회복했다.')
        self.ENG += self.RST
        print(f'{self.name}은(는) {self.RST}만큼 기력을 회복했다.',
              f'현재 기력: {self.ENG}', sep='\n')
        if target.HP <= 0:
            print(f'{target.name}이 대충 죽었다는 내용')
            self.HP += self.VIT*1.5
            print(f'{self.name}은(는) {self.VIT*1.5}만큼 체력을 회복했다.')
            self.ENG += self.RST*1.5
            print(f'{self.name}은(는) {self.RST*1.5}만큼 기력을 회복했다.',
                  f'현재 기력: {self.ENG}', sep='\n')
            print('================================================================================================')

        # 엎어치기
    def overthrow(self, target):
        damage = self.ATK*1.8
        damage -= target.DEF  # 방어력으로 물리공격 상쇄
        self.ENG -= 60
        print('60 기력사용')
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 오소이')
        target.HP -= damage
        print(f'{damage}만큼 바닥도 부서졌다!')
        self.HP += self.VIT
        print(f'{self.name}은(는) {self.VIT}만큼 체력을 회복했다.')
        self.ENG += self.RST
        print(f'{self.name}은(는) {self.RST}만큼 기력을 회복했다.',
              f'현재 기력: {self.ENG}', sep='\n')
        if target.HP <= 0:
            print(f'{target.name}녀석 바닥에 파묻힌채로 가버렸군')
            self.HP += self.VIT*1.5
            print(f'{self.name}은(는) {self.VIT*1.5}만큼 체력을 회복했다.')
            self.ENG += self.RST*1.5
            print(f'{self.name}은(는) {self.RST*1.5}만큼 기력을 회복했다.',
                  f'현재 기력: {self.ENG}', sep='\n')
            print('================================================================================================')


# 몬스터 기본스탯
class Monster:
    def __init__(self, name, HP, ATK, INT, DEF, REP, AGI, intro):
        self.name = name

        # 소모용
        self.max_HP = HP  # 최대체력
        self.HP = HP  # 체력

        # 고정스탯
        self.ATK = ATK  # 공격력
        self.INT = INT  # 지능/주문력
        self.DEF = DEF  # 방어력
        self.REP = REP  # 마법저항력
        self.AGI = AGI  # 민첩/회피율
        self.intro = intro


# Skeleton
        # 스켈레톤 평타


    def skeleton_attack(self, target):
        if random.random() < target.AGI:
            return
        damage = self.ATK + random.randint(-50, 70)  # 랜덤으로 치명타 적용
        damage -= target.DEF  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{self.name} : 오소이')
        target.HP -= damage
        print(f'Skeleton의 일반공격으로 {damage}만큼 데미지를 입었다!')
        if target.HP <= 0:
            print(f'Skeleton의 일반공격으로 {damage} 피해를 입고 영웅은 쓰러졌다!')
            print('아이고 이렇게 가면 이 세계는 누가지키나...')
            print('================================================================================================')

        # 화살
    def arrow(self, target):
        if random.random() < target.AGI:
            return
        damage = self.ATK
        damage -= target.DEF  # 방어력으로 물리공격 상쇄
        target.DEF -= 20
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{self.name} : 오소이')
        target.HP -= damage
        print(f'Skeleton의 화살로 {damage} 피해를 입고 방어력이 20 떨어졌다!',
              f'현재 방어력 : {target.DEF}', '\n')
        if target.HP <= 0:
            print(f'Skeleton의 화살로 {damage} 피해를 입고 영웅은 쓰러졌다!')
            print('아이고 이렇게 가면 이 세계는 누가지키나...')
            print('================================================================================================')


# Giant Fly
        # 거대파리 평타


    def giantfly_attack(self, target):
        if random.random() < target.AGI:
            return
        damage = self.ATK + random.randint(-50, 100)  # 랜덤으로 치명타 적용
        damage -= target.DEF  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{self.name} : 오소이')
        target.HP -= damage
        print(f'거대파리의 싸대기로 {damage}만큼 피해를 입었다!')
        if target.HP <= 0:
            print(f'거대파리의 싸대기로 {damage} 피해를 입고 영웅은 쓰러졌다!')
            print('아이고 이렇게 가면 이 세계는 누가지키나...')
            print('================================================================================================')

        # 박치기

    def headattack(self, target):
        if random.random() < target.AGI:
            return
        damage = self.ATK + 30
        damage -= target.DEF  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{self.name} : 오소이')
        target.HP -= damage
        print(f'거대파리의 박치기 공격으로 {damage}만큼 피해를 입었다!')
        if target.HP <= 0:
            print(f'거대파리의 박치기 공격으로 {damage} 피해를 입고 영웅은 쓰러졌다!')
            print('아이고 이렇게 가면 이 세계는 누가지키나...')
            print('================================================================================================')


# Beelzebub
        # 베엘제붑 평타

    def beelzebub_attack(self, target):
        if random.random() < target.AGI:
            return
        damage = self.ATK + random.randint(50, 130)  # 랜덤으로 치명타 적용
        damage -= target.DEF  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{self.name} : 오소이')
        target.HP -= damage
        print(f'베엘제붑의 지건으로 {damage}만큼 피해를 입었다!')
        if target.HP <= 0:
            print(f'베엘제붑의 지건으로 {damage} 피해를 입고 영웅은 쓰러졌다!')
            print('아이고 이렇게 가면 이 세계는 누가지키나...')
            print('================================================================================================')

        # 벌레공격

    def bugsattack(self, target):
        damage = self.INT*1.5
        damage -= target.REP  # 마법저항력으로 물리공격 상쇄
        target.HP -= damage
        target.REP -= self.INT*0.2
        self.HP -= self.INT*0.1
        print(f'베엘제붑은 자신의 살점을 때어 벌레공격으로 {damage}만큼 피해를 입고 마법저항력이 {self.INT*0.2} 떨어졌다!',
              f'현재 마법저항력 : {target.REP}', '\n')
        if target.HP <= 0:
            print(f'베엘제붑의 벌레공격으로 {damage} 피해를 입고 영웅은 쓰러졌다!')
            print('코이츠 구더기밥이 되어버린 wwww')
            print('================================================================================================')


# Spider
        # 거미 평타

    def spider_attack(self, target):
        if random.random() < target.AGI:
            return
        damage = self.ATK + random.randint(0, 80)  # 랜덤으로 치명타 적용
        damage -= target.DEF  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{self.name} : 오소이')
        target.HP -= damage
        print(f'거미에게 물려 {damage}만큼 피해를 입었다!')
        if target.HP <= 0:
            print(f'거미에게 물려 {damage} 피해를 입고 영웅은 쓰러졌다!')
            print('아이고 이렇게 가면 이 세계는 누가지키나...')
            print('================================================================================================')

        # 거미줄 공격

    def webattack(self, target):
        if random.random() < target.AGI:
            return
        damage = self.INT*1.2
        damage -= target.REP
        target.REP -= self.INT*0.1
        if damage < 0:
            damage = 0
            print(f'{self.name} : 오소이')
        target.HP -= damage
        print(f'거미줄 공격으로 {damage}만큼 피해를 입고 마법저항력이 {self.INT*0.1} 떨어졌다!',
              f'현재 마법저항력 : {target.REP}', '\n')
        if target.HP <= 0:
            print(f'거미줄 공격으로 {damage} 피해를 입고 영웅은 쓰러졌다!')
            print('아이고 이렇게 가면 이 세계는 누가지키나...')
            print('================================================================================================')


# Adam's Apple Snake
        # 뱀 평타

    def snakeattack(self, target):
        if random.random() < target.AGI:
            return
        damage = self.ATK + random.randint(0, 80)
        damage -= target.DEF
        if damage < 0:
            damage = 0
            print(f'{self.name} : 오소이')
        target.HP -= damage
        print(f'뱀한테 뺨맞고 {damage}만큼 피해를 입었다!')
        if target.HP <= 0:
            print(f'뱀한테 뺨맞고 {damage} 피해를 입고 영웅은 쓰러졌다!')
            print('아이고 이렇게 가면 이 세계는 누가지키나...')
            print('================================================================================================')

        # 침뱉기

    def spitting(self, target):
        damage = self.INT*1.2
        damage -= target.REP
        target.REP -= self.INT*0.1
        print(f'선악과뱀에게 침을 맞고 {damage}만큼 피해를 입고 마법저항력이 {self.INT*0.1} 떨어졌다!',
              f'현재 마법저항력 : {target.REP}', '\n')
        if target.HP <= 0:
            print(f'선악과뱀에게 침을 맞고 {damage} 피해를 입고 영웅은 쓰러졌다!')
            print(f'{target.name}, 이 곳에 침맞고 잠들다')
            print('================================================================================================')


# LILITH
        # 짓밟기

    def stompon(self, target):
        damage = self.ATK*0.3 + self.INT*1.5
        damage -= target.REP - target.DEF
        print(f'성역의 어머니에게 밟혀 {damage}만큼 피해를 입었다. 포상이다!')
        if target.HP <= 0:
            print(f'성역의 어머니에게 밟혀 {damage} 피해를 입고 영웅은 성불했다!', '마망!', sep='\n')
            print('성역의 어머니 LILITH, 이제 그녀를 막을 자는 아무도 없다!')
            print('================================================================================================')

        # 흡혈
    def lifeabsorption(self, target):
        damage = self.INT*2
        damage -= target.REP
        self.HP += damage*0.5
        print(f'체력흡수를 당해 {damage}만큼 피해를 입었고,', f'그녀는 {damage*0.5}만큼 체력을 회복했다!')
        if target.HP <= 0:
            print(f'{target.name}녀석... {damage} 피해를 입고 결국 모조리 흡수당하여 흔적조차 남지 않았어')
            print('================================================================================================')


# 자식클래스
# Sword Master Class
class Sword_Master(Character):
    def __init__(self, name, HP, MP, ENG, BLF, ATK, INT, FTH, DEF, REP, AGI, VIT, REM, RST):
        super().__init__(name, HP, MP, ENG, BLF, ATK,
                         INT, FTH, DEF, REP, AGI, VIT, REM, RST)

        # 소모용
        self.HP = HP  # 체력

        # 고정스탯
        self.ATK = ATK  # 공격력
        self.DEF = DEF  # 방어력
        self.REP = REP  # 마법저항력
        self.AGI = AGI  # 민첩/회피율
        self.VIT = VIT  # 체력재생력

        self.skills = [self.swordman_attack,
                       self.whirlwind, self.tearoffhead, self.spirited]

    def stats(self):
        stat_list = [
            f"체력: {self.HP}",
            f"마나: {self.MP}",
            f"기력: {self.ENG}",
            f"믿음: {self.BLF}",
            f"공격력: {self.ATK}",
            f"지능: {self.INT}",
            f"신앙력: {self.FTH}",
            f"방어력: {self.DEF}",
            f"마법저항력: {self.REP}",
            f"민첩: {self.AGI}",
            f"체력재생력: {self.VIT}",
            f"기력재생력: {self.RST}",
            f"마나재생력: {self.REM}"
        ]
        print(stat_list)

    def attack(self, target):
        while True:
            print("어떤 공격을 할까?")
            for i, skill in enumerate(self.skills):
                print(f"{i+1}: {skill.__name__}")  # 스킬 번호와 이름 출력
            try:
                choice = int(input()) - 1  # 스킬 번호 입력 받기 (인덱스는 0부터 시작하므로 1을 뺌)
                if 0 <= choice < len(self.skills):
                    selected_skill = self.skills[choice]  # 선택한 스킬의 함수 객체 가져오기
                    selected_skill(target)  # 선택한 스킬 사용하기
                    break  # 올바른 스킬을 선택했으므로 루프를 빠져나감
                else:
                    print("얘! 숫자 읽을줄 모르니?")
            except ValueError:
                print("오타 검지검지~")

# Holy Knight Class


class Holy_Knight(Character):
    def __init__(self, name, HP, MP, ENG, BLF, ATK, INT, FTH, DEF, REP, AGI, VIT, REM, RST):
        super().__init__(name, HP, MP, ENG, BLF, ATK,
                         INT, FTH, DEF, REP, AGI, VIT, REM, RST)

        # 소모용
        self.HP = HP  # 체력
        self.BLF = BLF  # 믿음/Holy Knight의 마나역할

        # 고정스탯
        self.ATK = ATK  # 공격력
        self.FTH = FTH  # 신앙력
        self.DEF = DEF  # 방어력
        self.REP = REP  # 마법저항력
        self.AGI = AGI  # 민첩/회피율
        self.VIT = VIT  # 체력재생력

        self.skills = [self.holy_attack,
                       self.sacredfire, self.holyvolt, self.pray]

    def attack(self, target):
        while True:
            print("어떤 공격을 할까?")
            for i, skill in enumerate(self.skills):
                print(f"{i+1}: {skill.__name__}")  # 스킬 번호와 이름 출력
            try:
                choice = int(input()) - 1  # 스킬 번호 입력 받기 (인덱스는 0부터 시작하므로 1을 뺌)
                if 0 <= choice < len(self.skills):
                    selected_skill = self.skills[choice]  # 선택한 스킬의 함수 객체 가져오기
                    selected_skill(target)  # 선택한 스킬 사용하기
                    break  # 올바른 스킬을 선택했으므로 루프를 빠져나감
                else:
                    print("얘! 숫자 읽을줄 모르니?")
            except ValueError:
                print("오타 검지검지~")

# Sorceress Class


class Sorceress(Character):
    def __init__(self, name, HP, MP, ENG, BLF, ATK, INT, FTH, DEF, REP, AGI, VIT, REM, RST):
        super().__init__(name, HP, MP, ENG, BLF, ATK,
                         INT, FTH, DEF, REP, AGI, VIT, REM, RST)

        # 소모용
        self.HP = HP  # 체력
        self.MP = MP  # 마나

        # 고정스탯
        self.ATK = ATK  # 공격력
        self.INT = INT  # 지능/주문력
        self.DEF = DEF  # 방어력
        self.REP = REP  # 마법저항력
        self.AGI = AGI  # 민첩/회피율
        self.VIT = VIT  # 체력재생력
        self.REM = REM  # 마나재생력

        self.skills = [self.sorceress_attack,
                       self.fireinthehole, self.icebreath, self.dirtgrave, self.healself]

    def attack(self, target):
        while True:
            print("어떤 공격을 할까?")
            for i, skill in enumerate(self.skills):
                print(f"{i+1}: {skill.__name__}")  # 스킬 번호와 이름 출력
            try:
                choice = int(input()) - 1  # 스킬 번호 입력 받기 (인덱스는 0부터 시작하므로 1을 뺌)
                if 0 <= choice < len(self.skills):
                    selected_skill = self.skills[choice]  # 선택한 스킬의 함수 객체 가져오기
                    selected_skill(target)  # 선택한 스킬 사용하기
                    break  # 올바른 스킬을 선택했으므로 루프를 빠져나감
                else:
                    print("얘! 숫자 읽을줄 모르니?")
            except ValueError:
                print("오타 검지검지~")

# Infighter Class


class Infighter(Character):
    def __init__(self, name, HP, MP, ENG, BLF, ATK, INT, FTH, DEF, REP, AGI, VIT, REM, RST):
        super().__init__(name, HP, MP, ENG, BLF, ATK,
                         INT, FTH, DEF, REP, AGI, VIT, REM, RST)

        # 소모용
        self.HP = HP  # 체력
        self.ENG = ENG  # 기력

        # 고정스탯
        self.ATK = ATK  # 공격력
        self.DEF = DEF  # 방어력
        self.REP = REP  # 마법저항력
        self.AGI = AGI  # 민첩/회피율
        self.VIT = VIT  # 체력재생력
        self.RST = RST  # 기력재생력

        self.skills = [self.infighter_attack,
                       self.sincerepunch, self.whirlkick, self.overthrow]

    def attack(self, target):
        while True:
            print("어떤 공격을 할까?")
            for i, skill in enumerate(self.skills):
                print(f"{i+1}: {skill.__name__}")  # 스킬 번호와 이름 출력
            try:
                choice = int(input()) - 1  # 스킬 번호 입력 받기 (인덱스는 0부터 시작하므로 1을 뺌)
                if 0 <= choice < len(self.skills):
                    selected_skill = self.skills[choice]  # 선택한 스킬의 함수 객체 가져오기
                    selected_skill(target)  # 선택한 스킬 사용하기
                    break  # 올바른 스킬을 선택했으므로 루프를 빠져나감
                else:
                    print("얘! 숫자 읽을줄 모르니?")
            except ValueError:
                print("오타 검지검지~")

# 몬스터 클래스

# Skeleton Class


class Skeleton(Monster):
    def __init__(self, name, HP, ATK, INT, DEF, REP, AGI, intro):
        super().__init__(name, HP, ATK, INT, DEF, REP, AGI, intro)
        self.name = name

        # 소모용
        self.HP = HP  # 체력

        # 고정스탯
        self.ATK = ATK  # 공격력
        self.DEF = DEF  # 방어력
        self.REP = REP  # 마법저항력
        self.AGI = AGI  # 민첩/회피율
        self.intro = intro  # 시작멘트

        self.skills = [self.skeleton_attack, self.arrow]
        self.attack_count = 0

    def attack(self, target):
        if self.attack_count < 3:
            self.skeleton_attack(target)
            self.attack_count += 1
        else:
            self.arrow(target)
            self.attack_count = 0

# Giant Fly


class Giant_Fly(Monster):
    def __init__(self, name, HP, ATK, INT, DEF, REP, AGI, intro):
        super().__init__(name, HP, ATK, INT, DEF, REP, AGI, intro)
        self.name = name

        # 소모용
        self.HP = HP  # 체력

        # 고정스탯
        self.ATK = ATK  # 공격력
        self.DEF = DEF  # 방어력
        self.REP = REP  # 마법저항력
        self.AGI = AGI  # 민첩/회피율
        self.intro = intro  # 시작멘트

        self.skills = [self.giantfly_attack, self.headattack]
        self.attack_count = 0

    def attack(self, target):
        if self.attack_count < 3:
            self.giantfly_attack(target)
            self.attack_count += 1
        else:
            self.headattack(target)
            self.attack_count = 0
# Beelzebub


class Beelzebub(Monster):
    def __init__(self, name, HP, ATK, INT, DEF, REP, AGI, intro):
        super().__init__(name, HP, ATK, INT, DEF, REP, AGI, intro)
        self.name = name

        # 소모용
        self.HP = HP  # 체력

        # 고정스탯
        self.ATK = ATK  # 공격력
        self.INT = INT  # 지능/주문력
        self.DEF = DEF  # 방어력
        self.REP = REP  # 마법저항력
        self.AGI = AGI  # 민첩/회피율
        self.intro = intro  # 시작멘트

        self.skills = [self.beelzebub_attack, self.bugsattack]
        self.attack_count = 0

    def attack(self, target):
        if self.attack_count < 3:
            self.beelzebub_attack(target)
            self.attack_count += 1
        else:
            self.bugsattack(target)
            self.attack_count = 0
# Spider


class Spider(Monster):
    def __init__(self, name, HP, ATK, INT, DEF, REP, AGI, intro):
        super().__init__(name, HP, ATK, INT, DEF, REP, AGI, intro)
        self.name = name

        # 소모용
        self.HP = HP  # 체력

        # 고정스탯
        self.ATK = ATK  # 공격력
        self.INT = INT  # 지능/주문력
        self.DEF = DEF  # 방어력
        self.REP = REP  # 마법저항력
        self.AGI = AGI  # 민첩/회피율
        self.intro = intro  # 시작멘트

        self.skills = [self.spider_attack, self.webattack]
        self.attack_count = 0

    def attack(self, target):
        if self.attack_count < 3:
            self.spider_attack(target)
            self.attack_count += 1
        else:
            self.webattack(target)
            self.attack_count = 0

# Adam's Apple Snake


class AAS(Monster):
    def __init__(self, name, HP, ATK, INT, DEF, REP, AGI, intro):
        super().__init__(name, HP, ATK, INT, DEF, REP, AGI, intro)
        self.name = name

        # 소모용
        self.HP = HP  # 체력

        # 고정스탯
        self.ATK = ATK  # 공격력
        self.INT = INT  # 지능/주문력
        self.DEF = DEF  # 방어력
        self.REP = REP  # 마법저항력
        self.AGI = AGI  # 민첩/회피율
        self.intro = intro  # 시작멘트

        self.skills = [self.snakeattack, self.spitting]
        self.attack_count = 0

    def attack(self, target):
        if self.attack_count < 3:
            self.snakeattack(target)
            self.attack_count += 1
        else:
            self.spitting(target)
            self.attack_count = 0
# LILITH


class LILITH(Monster):
    def __init__(self, name, HP, ATK, INT, DEF, REP, AGI, intro):
        super().__init__(name, HP, ATK, INT, DEF, REP, AGI, intro)
        self.name = name

        # 소모용
        self.HP = HP  # 체력

        # 고정스탯
        self.ATK = ATK  # 공격력
        self.INT = INT  # 지능/주문력
        self.DEF = DEF  # 방어력
        self.REP = REP  # 마법저항력
        self.AGI = AGI  # 민첩/회피율
        self.intro = intro  # 시작멘트

        self.skills = [self.stompon, self.lifeabsorption]
        self.attack_count = 0

    def attack(self, target):
        if self.attack_count < 5:
            self.stompon(target)
            self.attack_count += 1
        else:
            self.lifeabsorption(target)
            self.attack_count = 0


def battle():
    print('대충 세상이 거시기해서 거시기해졌으니 구해야한다는 내용의 나래이션')
    print("당신은 누구인가")
    name = input()
    print("무엇으로 살아가는가 (1: Sword Master, 2: Holy Knight, 3: Sorceress, 4: Infighter):")
    character_choice = int(input())

# (name, HP, MP, ENG, BLF, ATK, INT, FTH, DEF, REP, AGI, VIT, REM, RST)
    if character_choice == 1:
        player = Sword_Master(name, 500, 0, 0, 0, 150, 0,
                              0, 100, 80, 0.1, 10, 0, 0)
        print(player.name, ': 눈도 깜짝 안한다!')
    elif character_choice == 2:
        player = Holy_Knight(name, 480, 0, 0, 200, 90,
                             0, 80, 150, 80, 0.1, 8, 0, 0)
        print(player.name, ': Firs mother is coming')
    elif character_choice == 3:
        player = Sorceress(name, 350, 300, 0, 0, 60, 250,
                           0, 80, 60, 0.2, 10, 15, 0)
        print(player.name, ': 레비오우사 not 레비오사아~')
    elif character_choice == 4:
        player = Infighter(name, 650, 0, 400, 0, 100, 0,
                           0, 110, 110, 0.2, 30, 0, 10)
        print(player.name, ': 나는 최강이다')
    else:
        print("입력좀 제대로 해봐", '자 다음!', sep='\n')
        battle()

    # 몬스터 생성
# (name, HP, ATK, INT, DEF, REP, AGI, intro)
    monsters = [
        Skeleton("Skeleton", 250, 100, 0, 50, 100, 0.1, '달그락달그락'),
        Giant_Fly("Giant Fly", 130, 70, 0, 60, 120, 0.3, '에ㅔㅔㅔㅔㅔㅔㅔㅔㅔㅔㅔ엥'),
        Beelzebub("Beelzebub", 350, 70, 150, 80, 130, 0.1, '어? 나 아직 밥 안시켰는데'),
        Spider("Spider", 150, 130, 80, 100, 40, 0.1, '쉬이익! 쉬이익!'),
        AAS("Adam's Apple Snake", 180, 130, 50, 60, 80, 0.4, '사과 하나 먹을래?'),
        LILITH("LILITH", 1000, 60, 250, 100, 120, 0.1,
               '최초의 여성, 아담의 첫 번째 부인, 성역의 어머니 LILITH가 모습을 드러냈다!\n"내 아이들아, 족쇄를 벗고... 죄악 속에서 아름답게 거듭나라..."')
    ]

    # 전투 진행

    for monster in monsters:
        print(monster.name, ':', monster.intro)
        print(f'내 앞에서 알짱거리는 {monster.name}, 물리쳐야겠지? 아무래도...')
        while player.HP > 0 and monster.HP > 0:
            print(f"{player.name}: {player.HP}")
            print(f"{monster.name}: {monster.HP}")
            player.attack(monster)
            if monster.HP > 0:
                monster.attack(player)

        if player.HP <= 0:
            print("YOU DIED")
            print('리겜?')
            if int(input()) == 1:
                battle()
            else:
                break
        else:
            print(monster.name.upper(), 'GREAT ENEMY FELLED', '\n')

    if player.HP > 0:
        print("대충 세상을 구해서 잘했다는 내용의 아웃트로")


battle()
