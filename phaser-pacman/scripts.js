const config = {
    type: Phaser.AUTO,
    width: 800,
    height: 600,
    physics: {
        default: 'arcade',
        arcade: {
            gravity: { y: 200 }
        }
    },
    scene: {
        preload: preload,
        create: create
    }
}
const game = new Phaser.Game( config )

function preload() {

    //this.load.setBaseURL( 'http://labs.phaser.io' )
    this.load.image( 'spritesheet', 'assets/spritesheet.png' )
    //this.load.image( 'logo', 'assets/sprites/phaser3-logo.png' )
    //this.load.image( 'red', 'assets/particles/red.png' )

}

function create() {

    this.add.image( 400, 300, 'spritesheet' )

}
