namespace PiSync
{
    partial class AuthForm
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(AuthForm));
            panelAuth = new Panel();
            btnClose = new PictureBox();
            lblTitle = new Label();
            panel2 = new Panel();
            btnForgotPassword = new LinkLabel();
            btnLogin = new Button();
            label2 = new Label();
            tbPassword = new TextBox();
            label1 = new Label();
            tbUsername = new TextBox();
            pictureBox1 = new PictureBox();
            btnSetupIp = new PictureBox();
            panelAuth.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)btnClose).BeginInit();
            panel2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)pictureBox1).BeginInit();
            ((System.ComponentModel.ISupportInitialize)btnSetupIp).BeginInit();
            SuspendLayout();
            // 
            // panelAuth
            // 
            panelAuth.BackColor = Color.MediumPurple;
            panelAuth.Controls.Add(btnClose);
            panelAuth.Controls.Add(lblTitle);
            panelAuth.Dock = DockStyle.Top;
            panelAuth.Location = new Point(0, 0);
            panelAuth.Name = "panelAuth";
            panelAuth.Size = new Size(936, 79);
            panelAuth.TabIndex = 0;
            panelAuth.MouseDown += panelAuth_MouseDown;
            panelAuth.MouseMove += panelAuth_MouseMove;
            panelAuth.MouseUp += panelAuth_MouseUp;
            // 
            // btnClose
            // 
            btnClose.Anchor = AnchorStyles.Top | AnchorStyles.Right;
            btnClose.BackColor = Color.MediumPurple;
            btnClose.Cursor = Cursors.Hand;
            btnClose.Image = (Image)resources.GetObject("btnClose.Image");
            btnClose.Location = new Point(846, 17);
            btnClose.Name = "btnClose";
            btnClose.Size = new Size(40, 40);
            btnClose.SizeMode = PictureBoxSizeMode.Zoom;
            btnClose.TabIndex = 1;
            btnClose.TabStop = false;
            btnClose.Click += btnClose_Click;
            // 
            // lblTitle
            // 
            lblTitle.AutoSize = true;
            lblTitle.Font = new Font("Courier New", 16F);
            lblTitle.ForeColor = Color.Lavender;
            lblTitle.Location = new Point(39, 26);
            lblTitle.Name = "lblTitle";
            lblTitle.Size = new Size(381, 30);
            lblTitle.TabIndex = 0;
            lblTitle.Text = "AUTHENTICATION | PISYNC";
            lblTitle.MouseDown += lblTitle_MouseDown;
            lblTitle.MouseMove += lblTitle_MouseMove;
            lblTitle.MouseUp += lblTitle_MouseUp;
            // 
            // panel2
            // 
            panel2.Anchor = AnchorStyles.Top | AnchorStyles.Right;
            panel2.BackColor = Color.Lavender;
            panel2.Controls.Add(btnForgotPassword);
            panel2.Controls.Add(btnLogin);
            panel2.Controls.Add(label2);
            panel2.Controls.Add(tbPassword);
            panel2.Controls.Add(label1);
            panel2.Controls.Add(tbUsername);
            panel2.Location = new Point(502, 138);
            panel2.Name = "panel2";
            panel2.Size = new Size(369, 351);
            panel2.TabIndex = 1;
            // 
            // btnForgotPassword
            // 
            btnForgotPassword.AutoSize = true;
            btnForgotPassword.Cursor = Cursors.Hand;
            btnForgotPassword.Font = new Font("Courier New", 11F);
            btnForgotPassword.LinkColor = Color.MediumPurple;
            btnForgotPassword.Location = new Point(101, 284);
            btnForgotPassword.Name = "btnForgotPassword";
            btnForgotPassword.Size = new Size(186, 21);
            btnForgotPassword.TabIndex = 5;
            btnForgotPassword.TabStop = true;
            btnForgotPassword.Text = "Forgot Password?";
            btnForgotPassword.LinkClicked += btnForgotPassword_LinkClicked;
            // 
            // btnLogin
            // 
            btnLogin.BackColor = Color.MediumPurple;
            btnLogin.Cursor = Cursors.Hand;
            btnLogin.Location = new Point(45, 216);
            btnLogin.Name = "btnLogin";
            btnLogin.Size = new Size(289, 51);
            btnLogin.TabIndex = 4;
            btnLogin.Text = "LOGIN";
            btnLogin.UseVisualStyleBackColor = false;
            btnLogin.Click += btnLogin_Click;
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Font = new Font("Courier New", 11F);
            label2.Location = new Point(45, 122);
            label2.Name = "label2";
            label2.Size = new Size(109, 21);
            label2.TabIndex = 3;
            label2.Text = "Password:";
            // 
            // tbPassword
            // 
            tbPassword.Location = new Point(45, 149);
            tbPassword.Name = "tbPassword";
            tbPassword.PasswordChar = '●';
            tbPassword.PlaceholderText = "Enter password";
            tbPassword.Size = new Size(289, 34);
            tbPassword.TabIndex = 2;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Font = new Font("Courier New", 11F);
            label1.Location = new Point(45, 35);
            label1.Name = "label1";
            label1.Size = new Size(109, 21);
            label1.TabIndex = 1;
            label1.Text = "Username:";
            // 
            // tbUsername
            // 
            tbUsername.Location = new Point(45, 62);
            tbUsername.Name = "tbUsername";
            tbUsername.PlaceholderText = "Enter username";
            tbUsername.Size = new Size(289, 34);
            tbUsername.TabIndex = 0;
            // 
            // pictureBox1
            // 
            pictureBox1.Image = Properties.Resources.connectivity;
            pictureBox1.Location = new Point(86, 138);
            pictureBox1.Name = "pictureBox1";
            pictureBox1.Size = new Size(369, 351);
            pictureBox1.SizeMode = PictureBoxSizeMode.CenterImage;
            pictureBox1.TabIndex = 2;
            pictureBox1.TabStop = false;
            // 
            // btnSetupIp
            // 
            btnSetupIp.Anchor = AnchorStyles.Bottom | AnchorStyles.Right;
            btnSetupIp.BackColor = Color.GhostWhite;
            btnSetupIp.Cursor = Cursors.Hand;
            btnSetupIp.Image = (Image)resources.GetObject("btnSetupIp.Image");
            btnSetupIp.Location = new Point(884, 499);
            btnSetupIp.Name = "btnSetupIp";
            btnSetupIp.Size = new Size(40, 40);
            btnSetupIp.SizeMode = PictureBoxSizeMode.Zoom;
            btnSetupIp.TabIndex = 2;
            btnSetupIp.TabStop = false;
            btnSetupIp.Click += btnSetupIp_Click;
            // 
            // AuthForm
            // 
            AutoScaleDimensions = new SizeF(14F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = Color.GhostWhite;
            BackgroundImageLayout = ImageLayout.Center;
            ClientSize = new Size(936, 551);
            Controls.Add(btnSetupIp);
            Controls.Add(pictureBox1);
            Controls.Add(panel2);
            Controls.Add(panelAuth);
            Font = new Font("Courier New", 13.8F, FontStyle.Regular, GraphicsUnit.Point, 0);
            FormBorderStyle = FormBorderStyle.None;
            Margin = new Padding(5, 4, 5, 4);
            Name = "AuthForm";
            StartPosition = FormStartPosition.CenterScreen;
            Text = "Form1";
            panelAuth.ResumeLayout(false);
            panelAuth.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)btnClose).EndInit();
            panel2.ResumeLayout(false);
            panel2.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)pictureBox1).EndInit();
            ((System.ComponentModel.ISupportInitialize)btnSetupIp).EndInit();
            ResumeLayout(false);
        }

        #endregion

        private Panel panelAuth;
        private Panel panel2;
        private LinkLabel btnForgotPassword;
        private Button btnLogin;
        private Label label2;
        private TextBox tbPassword;
        private Label label1;
        private TextBox tbUsername;
        private Label lblTitle;
        private PictureBox btnClose;
        private PictureBox pictureBox1;
        private PictureBox btnSetupIp;
    }
}
