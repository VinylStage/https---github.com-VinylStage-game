import random

print("대충 오프닝멘트")
print("이름을 입력하세요")
player_name = input()
print(f'난세에 태어난 영웅, {player_name}은 대충 거시기 해서 거시기 한다.')


# 캐릭터기본스탯
class Character:
    def __init__(self, name, HP, MP, ENG, BLF, ATK, INT, FTH, DEF, REP, AGI, VIT, REM, RST):
        self.name = name

        # 소모용
        self.max_HP = HP  # 최대체력
        self.HP = HP  # 체력
        self.max_MP = MP  # 최대마나
        self.MP = MP  # 마나
        self.max_ENG = ENG  # 최대기력
        self.ENG = ENG  # 기력
        self.max_BLF = BLF  # 최대믿음 /Holy Knight의 마나역할
        self.BLF = BLF  # 믿음

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
        damage = self.ATK + self.INT + random.randint(-50, 100)  # 랜덤으로 치명타 적용
        damage -= target.DEF  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
        target.hp -= damage
        print(f'대충{target.name}에게 {damage}를 입혔다는 내용')
        if target.hp <= 0:
            print(f'{target.name}이 대충 죽었다는 내용')

    # 소용돌이
    def whirlwind(self, target):
        if random.random() < target.AGI:
            return
        damage = self.ATK*0.8
        damage -= target.DEF
        if damage < 0:
            damage = 0
        target.HP -= damage
        print(f'대충{target.name}에게 {damage}만큼 망가졌다!')
        if target.hp <= 0:
            print(f'{target.name}, 소용돌이로 가루가 되었다.')

    # 머리찢기
    def tearoffhead(self, target):
        if random.random() < target.AGI:
            return
        damage = self.ATK*1.2
        damage -= target.DEF
        if damage < 0:
            damage = 0
        target.HP -= damage
        print(f'대충{target.name}에게 {damage}만큼 머리가 찢어졌다!')
        if target.HP <= 0:
            print(f'{target.name}의 머리가 사라졌다!')

    # 기합
    def spirited(self, target):
        target.DEF -= 50
        self.DEF += 30
        self.HP += 50
        print(f'{target.name}은 겁에질려 방어력이 50만큼 떨어지고',
              '나는 30이 오르고 50만큼 체력을 회복했다!', sep='\n')
        if target.DEF <= 0:
            print(f'{target.name}이 겁에질려 그대로 쓰러졌다!')

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
        target.HP -= damage
        print(f'대충{target.name}에게 {damage}를 입혔다!')
        if target.hp <= 0:
            print(f'{target.name}이 성스로워졌다!')

        # 신성한불꽃
    def sacredfire(self, target):
        if random.random() < target.AGI:
            return
        damage = self.FTH*0.7
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
        target.HP -= damage
        print(f'대충{target.name}에게 {damage}만큼 뜨끈뜨끈해졌다!')
        if target.HP <= 0:
            print(f'{target.name}, 귀중한 단백질원이 되었다')

        # 신성한 빛줄기
    def holyvolt(self, target):
        if random.random() < target.AGI:
            return
        damage = self.FTH
        damage -= target.DEF  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
        target.HP -= damage
        print(f'대충{target.name}에게 {damage}빛을 보게했다!')
        if target.HP <= 0:
            print(f'{target.name}아 제발 밖에좀 나가서', '\n', '햇빛도 보고 좀 그래!')

        # 기도
    def pray(self):
        effect = self.HP + self.FTH*0.3
        print(f'{effect}만큼 회복했다!')

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
        target.hp -= damage
        print(f'대충{target.name}에게 {damage}만큼 톡!')
        if target.hp <= 0:
            print('너는 뭘해도 죽을놈이구나')

        # 구멍속불
    def fireinthehole(self, target):
        if random.random() < target.AGI:
            return
        damage = self.INT*0.6
        damage -= target.REP  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
        target.HP -= damage
        print(f'{target.name}자식 {damage}만큼 익었다@')
        if target.HP <= 0:
            print(f'{target.name}, 맛있는 냄새가 솔솔 피어오른다.')

        # 얼음숨결
    def icebreath(self, target):
        if random.random() < target.AGI:
            return
        damage = self.INT*0.5
        damage -= target.REP  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
        target.HP -= damage
        print(f'{target.name}놈 얼리고 {damage}를 입었다!')
        # 다음턴으로가기 구현
        if target.HP <= 0:
            print(f'{target.name}, 선채로 사망..!')

        # 묻어버리기
    def durt(self, target):
        if random.random() < target.AGI:
            return
        damage = self.INT*0.8
        damage -= target.DEF  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
        target.HP -= damage
        print(f'{target.name}녀석 {damage}피해를 입고 겨우 흙더미에서 나왔다')
        if target.HP <= 0:
            print(f'{target.name}, 생 매 장 ~')

# 인파이터
        # 인파 평타
    def infighter_attack(self, target):
        if random.random() < target.AGI:
            return
        damage = self.ATK + random.randint(-50, 200)  # 랜덤으로 치명타 적용
        damage -= target.DEF  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
        target.HP -= damage
        print(f'{damage} 톡!')
        if target.HP <= 0:
            print(f'톡 쳤더니 죽어버린 {target.name} 코이츠 wwwww')

        # 진심펀치
    def sincerepunch(self, target):
        if random.random() < target.AGI:
            return
        damage = self.ATK*0.7
        damage -= target.DEF  # 방어력으로 물리공격 상쇄
        target.DEF = target.DEF - self.ATK*0.3
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
        target.HP -= damage
        print(f'{damage}만큼 맞고 {self.ATK*0.3}만큼 방어력을 깎았다!')
        if target.DEF <= 0:
            print(f'{target.name}녀석 방어구가 부서지고 쓰러졌어!')
        elif target.HP <= 0:
            print(f'{target.name}, DOWN! {target.name}, DOWN!')

        # 회전차기
    def whirlkick(self, target):
        if random.random() < target.AGI:
            return
        damage = self.ATK*1.2
        damage -= target.DEF  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
        target.HP -= damage
        print(f'{damage}만큼 아픈 주먹!')
        if target.HP <= 0:
            print(f'{target.name}이 대충 죽었다는 내용')

        # 엎어치기
    def overthrow(self, target):
        damage = self.ATK*1.8
        damage -= target.DEF  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
        target.HP -= damage
        print(f'{damage}만큼 바닥도 부서졌다!')
        if target.HP <= 0:
            print(f'{target.name}녀석 바닥에 파묻힌채로 가버렸군')


# 몬스터 기본스탯
class Monster:
    def __init__(self, name, HP, ATK, INT, DEF, REP, AGI):
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


# Skeleton
        # 스켈레톤 평타

    def skeleton_attack(self, target):
        if random.random() < target.AGI:
            return
        damage = self.ATK + random.randint(-50, 70)  # 랜덤으로 치명타 적용
        damage -= target.DEF  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
        target.HP -= damage
        print(f'나는 {damage}만큼 데미지를 입었다!')

        # 화살
    def arrow(self, target):
        if random.random() < target.AGI:
            return
        damage = self.ATK
        damage -= target.DEF  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
        target.HP -= damage
        print(f'나는 화살을 맞아 {damage}만큼 데미지를 입었다!')
        if target.HP <= 0:
            print('아이고 이렇게 가면 이 세계는 누가지키나...')


# Giant Fly
        # 거대파리 평타

    def giantfly_attack(self, target):
        if random.random() < target.AGI:
            return
        damage = self.ATK + random.randint(-50, 100)  # 랜덤으로 치명타 적용
        damage -= target.DEF  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
        target.HP -= damage
        print(f'나는 {damage}만큼 데미지를 입었다!')
        if target.HP <= 0:
            print('아이고 이렇게 가면 이 세계는 누가지키나...')

        # 박치기
    def headattack(self, target):
        if random.random() < target.AGI:
            return
        damage = self.ATK + 30
        damage -= target.DEF  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
        target.HP -= damage
        print(f'나는 박치기 공격으로 {damage}만큼 데미지를 입었다!')
        if target.HP <= 0:
            print('아이고 이렇게 가면 이 세계는 누가지키나...')

# Beelzebub
        # 베엘제붑 평타
    def beelzebub_attack(self, target):
        if random.random() < target.AGI:
            return
        damage = self.ATK + random.randint(50, 130)  # 랜덤으로 치명타 적용
        damage -= target.DEF  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
        target.HP -= damage
        print(f'나는 {damage}만큼 데미지를 입었다!')
        if target.HP <= 0:
            print('아이고 이렇게 가면 이 세계는 누가지키나...')

        # 벌레공격
    def bugsattack(self, target):
        damage = self.INT*1.5
        damage -= target.REP  # 방어력으로 물리공격 상쇄
        target.HP -= damage
        print(f'나는 벌레공격으로 {damage}만큼 데미지를 입었다!')
        if target.HP <= 0:
            print('코이츠 구더기의 밥이 되어버린 wwww')

# Spider
        # 거미 평타
    def spider_attack(self, target):
        if random.random() < target.AGI:
            return
        damage = self.ATK + random.randint(0, 80)  # 랜덤으로 치명타 적용
        damage -= target.DEF  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
        target.HP -= damage
        print(f'나는 {damage}만큼 데미지를 입었다!')
        if target.HP <= 0:
            print('아이고 이렇게 가면 이 세계는 누가지키나...')

        # 거미줄 공격
    def webattack(self, target):
        if random.random() < target.AGI:
            return
        damage = self.INT*1.2
        damage -= target.REP
        if damage < 0:
            damage = 0
        target.HP -= damage
        print(f'나는 거미줄 공격으로 {damage}만큼 피해를 입었다!')
        if target.HP <= 0:
            print('아이고 이렇게 가면 이 세계는 누가지키나...')

# Adam's Apple Snake
        # 뱀 평타
    def snakeattack(self, target):
        if random.random() < target.AGI:
            return
        damage = self.ATK + random.randint(0, 80)
        damage -= target.DEF
        if damage < 0:
            damage = 0
        target.HP -= damage
        print(f'뱀한테 뺨맞고 {damage}만큼 피해를 입었다!')
        if target.HP <= 0:
            print('아이고 이렇게 가면 이 세계는 누가지키나...')

        # 침뱉기
    def spitting(self, target):
        damage = self.INT*1.2
        damage -= target.REP
        print(f'침을 맞고 {damage}만큼 피해를 입었다!')
        if target.HP <= 0:
            print(f'{target.name}, 이 곳에 침맞고 잠들다')

# LILITH
        # 짓밟기
    def stompon(self, target):
        damage = self.ATK*0.3 + self.INT*1.5
        damage -= target.REP, target.DEF
        print(f'성역의 어머니에게 밟히고 {damage}만큼 피해를 입었다. 포상이다!')
        if target.HP <= 0:
            print('성역의 어머니 LILITH, 이제 그녀를 막을 자는 아무도 없다!')
        # 흡혈

    def lifeabsorption(self, target):
        damage = self.INT*2
        damage -= target.REP
        self.HP += damage*0.5
        print(f'체력흡수를 당해 {damage}만큼 피해를 입었고,', f'그녀는 {damage*0.5}만큼 체력을 회복했다!')
        if target.HP <= 0:
            print(f'{target.name}녀석... 결국 모조리 흡수당하여 흔적조차 남지 않았다.')
