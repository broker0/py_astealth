from enum import IntEnum


class Messenger(IntEnum):
    """Messenger types for notifications."""
    Telegram = 1
    Viber = 2
    Discord = 3


class FigureKind(IntEnum):
    fkLine = 0
    fkEllipse = 1
    fkRectangle = 2
    fkDirection = 3
    fkText = 4


class FigureCoord(IntEnum):
    fcWorld = 0
    fcScreen = 1


class BrushStyle(IntEnum):
    bsSolid = 0
    bsClear = 1
    bsHorizontal = 2
    bsVertical = 3
    bsFDiagonal = 4
    bsBDiagonal = 5
    bsCross = 6
    bsDiagCross = 7


class Layer(IntEnum):
    RhandLayer = 0x01
    LhandLayer = 0x02
    ShoesLayer = 0x03
    PantsLayer = 0x04
    ShirtLayer = 0x05
    HatLayer = 0x06
    GlovesLayer = 0x07
    RingLayer = 0x08
    TalismanLayer = 0x09
    NeckLayer = 0x0A
    HairLayer = 0x0B
    WaistLayer = 0x0C
    TorsoLayer = 0x0D
    BraceLayer = 0x0E
    BeardLayer = 0x10
    TorsoHLayer = 0x11
    EarLayer = 0x12
    ArmsLayer = 0x13
    CloakLayer = 0x14
    BpackLayer = 0x15
    RobeLayer = 0x16
    EggsLayer = 0x17
    LegsLayer = 0x18
    HorseLayer =0x19
    RstkLayer = 0x1A
    NRstkLayer = 0x1B
    SellLayer =0x1C
    BankLayer = 0x1D


class EventType(IntEnum):
    EvItemInfo = 0
    EvItemDeleted = 1
    EvSpeech = 2
    EvDrawGamePlayer = 3
    EvMoveRejection = 4
    EvDrawContainer = 5
    EvAddItemToContainer = 6
    EvAddMultipleItemsInCont = 7
    EvRejectMoveItem = 8
    EvUpdateChar = 9
    EvDrawObject = 10
    EvMenu = 11
    EvMapMessage = 12
    EvAllowRefuseAttack = 13
    EvClilocSpeech = 14
    EvClilocSpeechAffix = 15
    EvUnicodeSpeech = 16
    EvBuffDebuffSystem = 17
    EvClientSendResync = 18
    EvCharAnimation = 19
    EvIcqDisconnect = 20
    EvIcqConnect = 21
    EvIcqIncomingText = 22
    EvIcqError = 23
    EvIncomingGump = 24
    EvTimer1 = 25
    EvTimer2 = 26
    EvWindowsMessage = 27
    EvSound = 28
    EvDeath = 29
    EvQuestArrow = 30
    EvPartyInvite = 31
    EvMapPin = 32
    EvGumpTextEntry = 33
    EvGraphicalEffect = 34
    EvIrcIncomingText = 35
    EvMessengerEvent = 36
    EvSetGlobalVar = 37
    EvUpdateObjStats = 38
    EvGlobalChat = 39
    EvWarDamage = 40
    EvContextMenu = 41


class Virtue(IntEnum):
    Compassion = 0x69
    Honesty = 0x6A
    Honor = 0x6B
    Humility = 0x6C
    Justice = 0x6D
    Sacrifice = 0x6E
    Spirituality = 0x6F
    Valor = 0x70


class Spell(IntEnum):
    # 1st circle
    Clumsy = 1
    CreateFood = 2
    FeebleMind = 3
    Heal = 4
    MagicArrow = 5
    NightSight = 6
    ReactiveArmor = 7
    Weaken = 8
    # 2nd circle
    Agility = 9
    Cunning = 10
    Cure = 11
    Harm = 12
    MagicTrap = 13
    MagicUntrap = 14
    Protection = 15
    Strength = 16
    # 3rd circle
    Bless = 17
    Fireball = 18
    MagicLock = 19
    Poison = 20
    Telekinesis = 21
    Teleport = 22
    Unlock = 23
    wallOfStone = 24
    # 4th circle
    ArchCure = 25
    ArchProtection = 26
    Curse = 27
    FireField = 28
    GreaterHeal = 29
    Lightning = 30
    ManaDrain = 31
    Recall = 32
    # 5th circle
    BladeSpirit = 33
    DispelField = 34
    Incognito = 35
    MagicReflection = 36
    SpellReflection = 36
    MindBlast = 37
    Paralyze = 38
    PoisonField = 39
    SummonCreature = 40
    # 6th circle
    Dispel = 41
    EnergyBolt = 42
    Explosion = 43
    Invisibility = 44
    Mark = 45
    MassCurse = 46
    ParalyzeField = 47
    Reveal = 48
    # 7th circle
    ChainLightning = 49
    EnergyField = 50
    FlameStrike = 51
    GateTravel = 52
    ManaVampire = 53
    MassDispel = 54
    MeteorSwarm = 55
    Polymorph = 56
    # 8th circle
    Earthquake = 57
    EnergyVortex = 58
    Resurrection = 59
    SummonAirElemental = 60
    SummonDaemon = 61
    SummonEarthElemental = 62
    SummonFireElemental = 63
    SummonWaterElemental = 64
    # Necromancy
    AanimateDead = 101
    BloodOath = 102
    CorpseSkin = 103
    CurseWeapon = 104
    EvilOmen = 105
    HorrificBeast = 106
    LichForm = 107
    MindRot = 108
    PainSpike = 109
    PoisonStrike = 110
    Strangle = 111
    SummonFamiliar = 112
    VampiricEmbrace = 113
    VengefulSpirit = 114
    Wwither = 115
    WraithForm = 116
    Exorcism = 117
    # Paladin spells
    CleanseByFire = 201
    CloseWounds = 202
    ConsecrateWeapon = 203
    DispelEvil = 204
    DivineFury = 205
    EnemyOfOne = 206
    HolyLight = 207
    NobleSacrifice = 208
    RemoveCurse = 209
    SacredJourney = 210
    # Bushido spells
    HonorableExecution = 401
    Confidence = 402
    Evasion = 403
    CounterAttack = 404
    LightningStrike = 405
    MomentumStrike = 406
    # Ninjitsu spells
    FocusAttack = 501
    DeathStrike = 502
    AnimalForm = 503
    KiAttack = 504
    SurpriseAttack = 505
    Backstab = 506
    ShadowJump = 507
    MirrorImage = 508
    # Spellweaving spells
    ArcaneCircle = 601
    GiftOfRenewal = 602
    ImmolatingWeapon = 603
    Attunement = 604
    Thunderstorm = 605
    NatureRury = 606
    SummonFey = 607
    SummonFiend = 608
    ReaperForm = 609
    Wildfire = 610
    EssenceOfWind = 611
    DryadAllure = 612
    EtherealVoyage = 613
    WwordOfDeath = 614
    GiftOfLife = 615
    AarcaneEmpowerment = 616
    # Mysticism spells
    NetherBolt = 678
    HealingStone = 679
    PureMagic = 680
    Enchant = 681
    Sleep = 682
    EeagleStrike = 683
    AnimatedWeapon = 684
    StoneForm = 685
    SpellTrigger = 686
    MassSleep = 687
    CleansingWinds = 688
    Bombard = 689
    SpellPlague = 690
    HailStorm = 691
    NetherCyclone = 692
    RisingColossus = 693
    # Shared Passives
    EnchantedSummoning = 715
    Intuition = 718
    WarriorsGifts = 733
    # Provocation
    Inspire = 701
    Invigorate = 702
    # Peacemaking
    Resilience = 703
    Perseverance = 704
    # Discordance
    Tribulation = 705
    Despair = 706
    # Magery
    DeathRay = 707
    EetherealBlast = 708
    # Mysticism
    NetherBlast = 709
    MysticWeapon = 710
    # Necromancy
    CommandUndead = 711
    Conduit = 712
    # Spellweaving
    ManaShield = 713
    Summonreaper = 714
    # Bushido
    AnticipateHit = 716
    WarCry = 717
    # Chivalry
    Rejuvenate = 719
    HolyFist = 720
    # Ninjitsu
    Shadow = 721
    WhiteTigerForm = 722
    # Archery
    FlamingShot = 723
    PlayingTheOdds = 724
    # Fencing
    Thrust = 725
    Pierce = 726
    # Mace Fighting
    Stagger = 727
    Toughness = 728
    # Swordsmanship
    Onslaught = 729
    FocusedEye = 730
    # Throwing
    ElementalFury = 731
    CalledShot = 732
    # Parrying
    ShieldBash = 734
    Bodyguard = 735
    HeightenSenses = 736
    # Poisoning
    Tolerance = 737
    InjectedStrike = 738
    Potency = 739
    # Wrestling
    Rampage = 740
    FistsOfFury = 741
    Knockout = 742
    # Animal Taming
    Whispering = 743
    Boarding = 745
    CombatTraining = 744

