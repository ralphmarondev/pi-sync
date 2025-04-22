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
            panel1 = new Panel();
            label3 = new Label();
            panel2 = new Panel();
            btnForgotPassword = new LinkLabel();
            btnLogin = new Button();
            label2 = new Label();
            tbPassword = new TextBox();
            label1 = new Label();
            tbUsername = new TextBox();
            panel1.SuspendLayout();
            panel2.SuspendLayout();
            SuspendLayout();
            // 
            // panel1
            // 
            panel1.BackColor = Color.MediumPurple;
            panel1.Controls.Add(label3);
            panel1.Dock = DockStyle.Top;
            panel1.Location = new Point(0, 0);
            panel1.Name = "panel1";
            panel1.Size = new Size(936, 79);
            panel1.TabIndex = 0;
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Font = new Font("Courier New", 16F);
            label3.ForeColor = Color.Lavender;
            label3.Location = new Point(39, 26);
            label3.Name = "label3";
            label3.Size = new Size(381, 30);
            label3.TabIndex = 0;
            label3.Text = "AUTHENTICATION | PISYNC";
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
            tbUsername.Size = new Size(289, 34);
            tbUsername.TabIndex = 0;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(14F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(936, 551);
            Controls.Add(panel2);
            Controls.Add(panel1);
            Font = new Font("Courier New", 13.8F, FontStyle.Regular, GraphicsUnit.Point, 0);
            FormBorderStyle = FormBorderStyle.None;
            Margin = new Padding(5, 4, 5, 4);
            Name = "Form1";
            Text = "Form1";
            panel1.ResumeLayout(false);
            panel1.PerformLayout();
            panel2.ResumeLayout(false);
            panel2.PerformLayout();
            ResumeLayout(false);
        }

        #endregion

        private Panel panel1;
        private Panel panel2;
        private LinkLabel btnForgotPassword;
        private Button btnLogin;
        private Label label2;
        private TextBox tbPassword;
        private Label label1;
        private TextBox tbUsername;
        private Label label3;
    }
}
